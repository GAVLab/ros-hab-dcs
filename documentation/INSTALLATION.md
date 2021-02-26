# Installation

## Installation Instructions

### Set Up the Pi (Basics)

* Download and flash microSD with Ubuntu Mate 20.04 Raspberry Pi 32-bit (ubuntu-mate-20.04.1-desktop-armhf%2Braspi.img.xz): https://releases.ubuntu-mate.org/focal/armhf/
* Connect to AU_WiFi (if on Auburn University's network): http://www.eng.auburn.edu/admin/ens/helpdesk/on-campus/wireless.html
* Install ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu

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
  
### Install ROS

 * Install ROS Noetic with this tutorial: http://wiki.ros.org/noetic/Installation/Ubuntu
 * ROS Desktop (not full) is sufficient.
 * Install Python
 ```
 sudo apt-get install python3

  
### Set Up i2c on Pi

* Enable i2c
  
  ```bash
  sudo apt-get install i2c-tools
  i2cdetect -l
  ```

* Add `i2c-devl` to boot with `sudo nano /etc/modules-load.d/modules.conf`
* Install wiringpi `sudo apt install wiringpi`
* Connect i2c devices to Sparkfun Qwiic hat and run `i2cdetect -y 1` to identify channels
* Install Circuit Python: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
* Install driver for BNO055 IMU: `sudo pip3 install adafruit-circuitpython-bno055`.
* Install driver for MPL3115A2 Baro/Temp/Alt Sensor: `sudo pip3 install adafruit-circuitpython-mpl3115a2`.
* Install driver for ICM20948 IMU: `sudo pip3 install sparkfun-qwiic-icm20948`.
* Slow down baud rate by adding `dtparam=i2c_baudrate=10000` with `sudo nano /boot/firmware/usercfg.txt`
* Ensure proper permissions to prevent i/o errors: 

```
cd /dev
sudo chmod og+rwx gpio*
```

### Set Up Cameras

* ROS Libraries

```bash
sudo apt-get install -y ros-noetic-camera-info-manager ros-noetic-rqt-image-view ros-noetic-compressed-image-transport ros-noetic-dynamic-reconfigure
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
roslaunch ~/ros-hab-dcs/launches/cameras.launch
rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.022 image:=/side_cam/image_raw camera:=/side_cam
rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.022 image:=/down_cam/image_raw camera:=/down_cam
```

### Setting Up the Arduino (SN01 variant only)

* Download Arduino IDE onto Raspberry Pi (Linux ARM 32-bits): https://www.arduino.cc/en/software
* Install IDE

  ```bash
  cd Downloads/
  tar -xf arduino-1.8.3-linuxarm.tar.xz
  sudo mv arduino-1.8.3 /opt
  sudo /opt/arduino-1.8.3/install.sh
  ```
* Identify USB port for Arduino in Arduino IDE and edit launch files in `~/ros-hab-dcs`

### Setting Up the GPS

* Install ROS NMEA libary: `sudo apt-get install -y ros-noetic-nmea-navsat-driver`
* Fix decoding error by using `sudo nano /opt/ros/noetic/lib/python3/dist-packages/libnmea_navsat_driver/nodes/nmea_serial_driver.py` and changing the `decode('utf-8')` to `decode(encodings='utf-8',errors='ignore')`. (Issue #115 of https://github.com/ros-drivers/nmea_navsat_driver)

## Running system

```bash
cd  ~/ros-hab-dcs/launches/
roslaunch full_flight.launch
./record.sh
```
