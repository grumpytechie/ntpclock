# ntpclock

This project uses a Raspberry Pi show NTP diciplned time on 6 7-Segment LED displays

## Bill of Materials

* 6 [SparkFun Large Digit Drivers](https://www.sparkfun.com/products/13279) 
* 6 [SparkFun 6.5" 7-Segment Displays](https://www.sparkfun.com/products/8530) 
* 1 Raspberry Pi 
* 1 [SparkFun Logic Level Converter](https://www.sparkfun.com/products/12009)
* 5 VDC power supply capable of 3 A
* 12 VDC power supply capable of 2 A

## Setting up NTP

First, we need to set up NTP on the Raspberry Pi.

`sudo apt-get install ntp`

Then, if you want to, you can configure your own time servers in `/etc/ntp.conf`, but it will work just fine with the stock Debian NTP Pool servers.
`sudo nano /etc/ntp.conf`

After changing the NTP conf, you need to restart the NTP deamon

`sudo /etc/init.d/ntpd restart`

Make sure your clock is running correctly by running the `date` command

`date`

Also remember to set your timezone

`sudo dpkg-reconfigure tzdata`

## Copying the Repository

## Setting the Python Code to Run at Startup

Copy the ntpclock.sh file to an appropriate directory on you Raspberry Pi, in my example I've created a new folder under /usr/local/ named ntpclock

Edit /etc/rc.local

`sudo nano /etc/rc.local`

and add the following line to the bottom

`/usr/local/ntpclock/ntpclock.sh &`


## Wiring Everything Up
