# Raspberry DHT11

> This project uses an RPi to read humidity and temperature from a dht11 sensor, then display in a lcd display

## List of materials

* Raspberry pi3
* DHT11 sensor
* LCD display i2c

## Connections

First lets connect the components as shown bellow

![connections](/fritzing/connections.png)

## Raspberry Setup

Once we installed the OS on the sd card [as described here](https://www.raspberrypi.org/documentation/installation/installing-images/) we should enable a means to program the RPi, for this task we will enable SSH access and configure our RPI so it can connect to our wifi network, and we can reach it, [instructions here](https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup)

## Developer tools

To make it easy to develop I recommend to install VScode on our computers, then install the remote ssh extensions

* https://code.visualstudio.com/
* https://code.visualstudio.com/docs/remote/ssh

## Develop the code

Now we can connect to our raspberry with the following code.

``` BASH
$ ssh pi@raspberrypi.local #password: raspberry
```

when promted we should type our password
Now VScode should open a new window where we can have access to our files and it will show some terminal tabs where we can put the commands required to try our code.

## Requirements

In order to make it death simple we need to install the libraries to manage the DHT11 sensor, open a terminal and type:

``` BASH
$ sudo pip install Adafruit_DHT
```

## Sources

DHT11 with raspberry
https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity/python-code

I2C Display with raspberry
https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

## Development

The following scripts were developed

**lcd_test.py**
: Simple code to test the LCD, once it is run, see what it the display showing

**dht11_test.py**
: Simple code to read the sensor and show values on terminal

**dht_lcd.py**
: Script that integrates the codes explained before, to read data from sensor and print on the LCD

**I2C_LCD_driver.py**
: Driver to be able to handle the LCD display

## Run scripts

``` BASH
$ sudo python dht_lcd.py 
```
**

## Run script automatically from boot

Edit the `` `/etc/rc.local` ` ` file, add the following line before the ` ``exit 0


``` BASH
sudo python /home/pi/dht_lcd.py 
```
