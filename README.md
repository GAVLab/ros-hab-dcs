# ros-hab-dcs

Robot Operating System (ROS) High Altitude Balloon (HAB) Data Collection System (DCS)

**Status:** Development In-Progress

## Introduction

This is a system to collect a high altitude balloon dataset utilizing ROS for aerial navigation algorithmic development.  The datasets contain downward facing visual imagery, side-facing imagery, IMU, GPS, internal and external barometric pressure, and internal and external temperature.  The system is designed to run Ubuntu Mate 20.04LTS with ROS Noetic Ninjemys on a Raspberry Pi 4 2GB and an Arduino Sense 33BLE.

## Installation Instructions

### Setting Up the Pi

* Download and flash microSD with Ubuntu Mate 20.04 Raspberry Pi 32-bit (ubuntu-mate-20.04.1-desktop-armhf%2Braspi.img.xz): https://releases.ubuntu-mate.org/focal/armhf/
* Connect to AU_WiFi (if on Auburn University's network): http://www.eng.auburn.edu/admin/ens/helpdesk/on-campus/wireless.html#:~:text=The%20Auburn%20University%20wireless%20network,able%20to%20browse%20the%20internet

### Setting Up the Arduino

* Use this guide: https://www.arduino.cc/en/Guide/NANO33BLESense
* In Tools > Library Manager install the following
  * ArduinoBLE
  * Nano33BLESensor

## Electrical Hardware

**System Diagram**

<img src="diagrams/system_diagram.png"
     style="width:500px;" />

**Arduino Protoboard Schematic**

<img src="diagrams/arduino_pinout_diagram.png"
     style="width:500px;" />