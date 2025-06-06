# ntpclock

This project uses a Raspberry Pi to show NTP disciplined time on 6 7-Segment LED displays

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

After changing the NTP conf, you need to restart the NTP daemon.

`sudo systemctl restart ntp`

Or on older systems using init.d:

`sudo /etc/init.d/ntpd restart`

Make sure your clock is running correctly by running the `date` command.

`date`

Also, remember to set your timezone.

`sudo dpkg-reconfigure tzdata`

## Copying the Repository

## Setting the Python Code to Run at Startup

### Crontab Method
Copy the `7seg_clock.py` file to an appropriate directory on your Raspberry Pi. In my example, I've created a new folder under `/usr/local/` named `ntpclock`

Edit /etc/crontab

`sudo nano /etc/crontab`

Add the following line to the bottom:  

`@reboot  root python /usr/local/ntpclock/7seg_clock.py &` 

### rc.local Method - Deprecated since Debian Bookworm
Copy the `ntpclock.sh` file to an appropriate directory on your Raspberry Pi, in my example, I've created a new folder under `/usr/local/` named `ntpclock`

Edit /etc/rc.local

`sudo nano /etc/rc.local`

Add the following line to the bottom

`/usr/local/ntpclock/ntpclock.sh &`


## Wiring Everything Up

![Wiring Diagram](clock-wiring.PNG?raw=true "Wiring Diagram")
