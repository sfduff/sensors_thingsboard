#!/bin/bash

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
