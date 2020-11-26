# ros-hab-dcs

Robot Operating System (ROS) High Altitude Balloon (HAB) Data Collection System (DCS)

**Status:** Development In-Progress

## Introduction

This is a system to collect a high altitude balloon dataset utilizing ROS for aerial navigation algorithmic development.  The datasets contain downward facing visual imagery, side-facing imagery, IMU, GPS, internal and external barometric pressure, and internal and external temperature.  The system is designed to run Ubuntu Mate 20.04LTS with ROS Noetic Ninjemys on a Raspberry Pi 4 2GB and an Arduino Sense 33BLE.

## Installation Instructions

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
  
### Setting Up i2c on Pi
* Enable i2c
  ```
  sudo apt-get install i2c-tools
  i2cdetect -l
  ```
* Add `i2c-devl` to boot with `sudo nano /etc/modules-load.d/modules.conf`
* Install wiringpi `sudo apt install wiringpi`
* Connect i2c devices to Sparkfun Qwiic hat and run `i2cdetect-y` to identify channels
* Install Circuit Python: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
* Install driver for BNO055 IMU: `sudo pip3 install adafruit-circuitpython-bno055`.
* Install driver for MPL3115A2 Baro/Temp/Alt Sensor: `sudo pip3 install adafruit-circuitpython-mpl3115a2`.
  
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

## Electrical Hardware

**System Diagram**

<img src="diagrams/system_diagram.png"
     style="width:500px;" />

**Arduino Protoboard Schematic**

<img src="diagrams/arduino_pinout_diagram.png"
     style="width:500px;" />