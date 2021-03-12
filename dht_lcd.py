#!/usr/bin/python
from time import *
import I2C_LCD_driver
import Adafruit_DHT
mylcd = I2C_LCD_driver.lcd()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    temperature_f = temperature*9/5 + 32
    line1='Temp: %2.0f C  %2.0f F'%(temperature, temperature_f)
    line2='Hum: %2.0f%% Mohsin'%humidity
    mylcd.lcd_display_string(line1, 1)
    mylcd.lcd_display_string(line2, 2)