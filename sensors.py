import smbus2
import bme280
import mh_z19
import time
import paho.mqtt.client as mqtt
import json



port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
    #data.id)
    #data.timestamp)
    #data.temperature)
    #data.pressure)
    #data.humidity)

sensor_data = {'temperature': 0, 'pressure' : 0, 'humidity': 0, 'co2': 0}

thingsboard_host = '192.168.1.101'
access_token = 'jCFMNG7wD6p6hX9S9FKC'
reading_interval = 5

client = mqtt.Client()
client.username_pw_set(access_token)
client.connect(thingsboard_host, 1883, 60)
client.loop_start()


try:
    while True:
        data = bme280.sample(bus, address, calibration_params)
        co2  = mh_z19.read()

        sensor_data['temperature'] = round(data.temperature,2)
        sensor_data['humidity'] = round(data.humidity,2)
        sensor_data['pressure'] = round(data.pressure,2)
        sensor_data['co2'] = co2['co2']

        print( sensor_data )

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        time.sleep(reading_interval)

except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
