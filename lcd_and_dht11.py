#!/usr/bin/python
from time import sleep
import Adafruit_CharLCD as LCD
import Adafruit_DHT

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

#Init LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message('Hello Mohsin!\n >>>> >>>')
lcd.clear()
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    temp_f = temperature*9/5 + 32
    message = 'Temp: %2.0fC %2.0fF\nHum: %2.1f%%'%(temperature, temp_f, humidity)
    print(message)
    lcd.message(message)
    lcd.clear()