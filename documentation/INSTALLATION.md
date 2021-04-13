# Installation

## Installation Instructions

### Set Up the Pi (Basics)

* Download and flash microSD with Ubuntu Mate 20.04 Raspberry Pi 64-bit
* Connect to AU_WiFi (if on Auburn University's network): http://www.eng.auburn.edu/admin/ens/helpdesk/on-campus/wireless.html

### Clone repository and get submodules

```bash
git clone https://github.com/GAVLab/ros-hab-dcs --recursive
```

If you are having trouble with submodules try the following commands

```bash
git submodule update --init --recursive
```

### Set Up VNC on the Pi (Optional)

* Install ifconfig and x11vnc: `sudo apt-get install net-tools x11vnc`
* Run `ifconfig` to identify ip address.
* Start the VNC

  ```bash
    startx &
    x11vnc &
  ```

* Login to VNC viewer with IP address
  
### Install ROS and other Basics

 * Install ROS Noetic with this tutorial: http://wiki.ros.org/noetic/Installation/Ubuntu
 * ROS Desktop (not full) is sufficient.
 * Add repository to .bashrc
 ```
 echo "source ~/ros-hab-dcs/catkin_ws/devel/setup.bash" >> ~/.bashrc
 source ~/.bashrc
 ```
 * Install Python 3
 ```
 sudo apt-get install python3
 ```

### Fix raspi_cpu_temp node
* Open `~/ros-hab-dcs/catkin_ws/src/raspi_cpu_temp/scripts/raspi_cpu_temp_node.py`
* Change first line to `#!/usr/bin/env python3`
  
### Set Up i2c on Pi

* Enable i2c
  
  ```bash
  sudo apt-get install i2c-tools
  i2cdetect -l
  ```

* Add `i2c-devl` to boot with `sudo nano /etc/modules-load.d/modules.conf`
* Slow down baud rate by adding `dtparam=i2c_baudrate=10000` with `sudo nano /boot/firmware/usercfg.txt`
* Install wiringpi `sudo apt install wiringpi`
* Ensure proper permissions to prevent i/o errors: 
```
cd /dev
sudo chmod og+rwx gpio*
```
* Connect i2c devices to Sparkfun Qwiic hat and run `i2cdetect -y 1` to identify channels
* Install Circuit Python: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
* Install driver for various sensors: `sudo pip3 install adafruit-circuitpython-bno055 adafruit-circuitpython-mpl3115a2 sparkfun-qwiic-icm20948 adafruit-circuitpython-ina219` 


### Setup UART  on Pi
* Follow the instructions found here: https://raspberrypi.stackexchange.com/questions/114366/rpi4-serial-port-not-working-on-either-raspberry-os-or-ubuntu
* Enable UART Permissions
```bash
sudo adduser $USER tty
sudo adduser $USER dialout 
sudo chmod g+r /dev/ttyAMA0
sudo chmod g+r /dev/ttyUSB0
```

### Setting Up the GPS

* Install ROS ublox: `sudo apt install ros-noetic-ublox`

### Set Up Cameras

* ROS Libraries

```bash
sudo apt-get install -y ros-noetic-camera-info-manager ros-noetic-rqt-image-view ros-noetic-compressed-image-transport ros-noetic-dynamic-reconfigure ros-noetic-usb-cam
```

* Enable CSI Camera
  ```sudo modprobe bcm2835-v4l2```
* Check video ports
  ```v4l2-ctl --list-devices```
* View Results once Running Node
  ```rqt_image_view```
* Setup library for camera calibration
  ```sudo apt-get install ros-noetic-image-geometry```
* Perform camera calibration. Move checkerboard paper until all bars are green and press "Calibrate" wait until results are printed to terminal (may take up to 10 minutes).  Press save (may take up to 5 minutes).  Press commit.

```bash
roslaunch ~/ros-hab-dcs/launches/sensors/camera_calib.launch
rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.022 image:=/down_cam/image_raw camera:=/down_cam
```


## Running system

```bash
cd  ~/ros-hab-dcs/launches/
roslaunch full_flight.launch
./record.sh
```
