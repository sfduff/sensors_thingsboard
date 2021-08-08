#!/bin/bash

# enable ports
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_serial 0

# install prerequisites
sudo apt-get install i2c-tools python3-pip -y
sudo pip3 install RPi.bme280 mh-z19 smbus2 paho-mqtt

# allow access to serial port for non root
# sudo chmod 777 /dev/serial0

# setup sensor service
sudo cp sensors.service /lib/systemd/system/.
sudo systemctl enable sensors.service
sudo systemctl daemon-reload
sudo systemctl start sensors.service
sudo systemctl status sensors.service
