# ros-hab-dcs

Robot Operating System (ROS) High Altitude Balloon (HAB) Data Collection System (DCS)

**Status:** Development In-Progress

## Introduction

This is a system to collect a high altitude balloon dataset utilizing ROS for aerial navigation algorithmic development.  The datasets contain downward facing visual imagery, side-facing imagery, IMU, GPS, internal and external barometric pressure, and internal and external temperature.  The system is designed to run Ubuntu Mate 20.04LTS with ROS Noetic Ninjemys on a Raspberry Pi 4 2GB and an Arduino Sense 33BLE.

## Installation Instructions

### Clone repository and get submodules

```
git clone https://github.com/GAVLab/ros-hab-dcs
git submodule update --init --recursive
```

### Set Up the Pi (Basics)

* Download and flash microSD with Ubuntu Mate 20.04 Raspberry Pi 32-bit (ubuntu-mate-20.04.1-desktop-armhf%2Braspi.img.xz): https://releases.ubuntu-mate.org/focal/armhf/
* Connect to AU_WiFi (if on Auburn University's network): http://www.eng.auburn.edu/admin/ens/helpdesk/on-campus/wireless.html
* Install ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu

### Set Up VNC on the Pi

* Install ifconfig: `sudo apt-get install net-tools`
* Install x11vnc: `sudo apt-get install x11vnc`
* Run `ifconfig` to identify ip address.
* Start the VNC

  ``` 
    startx &
    x11vnc &
  ```

* Login to VNC viewer with IP address
  
### Set Up i2c on Pi

* Enable i2c
  
  ```
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

### Set Up Cameras

* ROS Libraries
```
sudo apt-get install ros-noetic-camera-info-manager
sudo apt-get install ros-noetic-image-view
sudo apt-get install ros-noetic-compressed-image-transport
sudo apt-get install ros-noetic-dynamic-reconfigure
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
```
roslaunch ~/ros-hab-dcs/launches/cameras.launch
rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.022 image:=/side_cam/image_raw camera:=/side_cam
rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.022 image:=/down_cam/image_raw camera:=/down_cam```

### Setting Up the Arduino

* Download Arduino IDE onto Raspberry Pi (Linux ARM 32-bits): https://www.arduino.cc/en/software
* Install IDE
  ```
  cd Downloads/
  tar -xf arduino-1.8.3-linuxarm.tar.xz
  sudo mv arduino-1.8.3 /opt
  sudo /opt/arduino-1.8.3/install.sh
  ```
* In `Tools > Board > Boards Manager...`, install Arduino nRF528x Boards (Mbed OS).  This may take a few minutes.
* Select `Tools > Board > Arduino Mbed OS Boards > Arduino Nano 33 BLE`
* Select the proper port and test the Arduino with `File > Examples > Basics > Blink`
  * Example: `/dev/ttyACM0`
* In `Tools > Manage Libraries...` install the following
  * ArduinoBLE
  * Nano33BLESensor (Install all required libraries)

## Running system

  ```
  cd ~/ros-hab-dcs/catkin_ws
  source devel/setup.bash
  catkin_make
  roslaunch ~/ros-hab-dcs/launches/full_flight.launch`
  ```

## Electrical Hardware

**System Diagram**

<img src="diagrams/system_diagram.png"
     style="width:500px;" />

**Arduino Protoboard Schematic**

<img src="diagrams/arduino_pinout_diagram.png"
     style="width:500px;" />
