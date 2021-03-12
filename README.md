# Raspberry DHT11
> This project uses an RPi to read humidity and temperature from a dht11 sensor, then display in a lcd display

## List of materials
- Raspberry pi3
- DHT11 sensor
- LCD display i2c

## Connections
First lets connect the components as shown bellow
![connections](/fritzing/connections.png)

## Raspberry Setup
Once we installed the OS on the sd card [as described here](https://www.raspberrypi.org/documentation/installation/installing-images/) we should enable a means to program the RPi, for this task we will enable SSH access and configure our RPI so it can connect to our wifi network, and we can reach it, [instructions here](https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup)

## Developer tools
To make it easy to develop I recommend to install VScode on our computers, then install the remote ssh extensions
- https://code.visualstudio.com/
- https://code.visualstudio.com/docs/remote/ssh

## Develop the code
Now we can connect to our raspberry with the following code.
``` BASH
$ ssh pi@raspberrypi.local #password: raspberry
```
when promted we should type our password
Now VScode should open a new window where we can have access to our files and it will show some terminal tabs where we can put the commands required to try our code.

## Requirements
 