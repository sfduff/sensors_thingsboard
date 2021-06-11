# sensors_thingsboard

Supports both BME280 (temperature, relative humidity and atmospheric pressure) and MH-Z19 (co2) sensors conected to a single device.


# Connecting sensors

BME280 to rpi pins

  1 - 3v vin power
  
  3 - SDA1 i2c
  
  5 - SCL1 i2c
  
  9 - Ground


MH-Z19 to rpi pins

  2 - 5v vin power
  
  6 - Ground
  
  8 - UART0 TXD
  
  10 - UART0 RXD


# OS installation

Start with a fresh installation of Raspberry PI OS Lite

''sudo raspi-config''

Enalbe the i2c and serial interfaces


# Update and reboot host
``sudo apt-get update -y && sudo apt-get upgrade -y && sudo reboot now``


# Install drivers and software 
``sudo apt-get install  i2c-tools  python3-pip  i2c-tools  git  -y``

``sudo pip3 install  RPi.bme280 mh-z19  smbus2  paho-mqtt``


# clone repo and run 
``python3 read_bme280.py``
