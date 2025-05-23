# ntpclock
#
# A simple Raspberry Pi project that uses shift registers to
# display time on 7-segment displays.
#
# Copyright 2017-2025 GrumpyTechie.net
# Licensed under the EUPL

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin definitions for shift registers
ClockPin = 27
DataPin = 17
LatchPin = 22

GPIO.setup(DataPin, GPIO.OUT) # Serial Data Line
GPIO.setup(ClockPin, GPIO.OUT) # Clock Line
GPIO.setup(LatchPin, GPIO.OUT) # Latch Line

# Drive pins low initially
GPIO.output(DataPin,GPIO.LOW)
GPIO.output(ClockPin,GPIO.LOW)
GPIO.output(LatchPin,GPIO.LOW)

# Time for switching between time and date in seconds

DateTime = 5

# Segments definitions for SparkFun Large Digit Driver
#
# Standard 7-segment layout is the following
#
# **aaaa**
# *f****b*
# *f****b*
# **gggg**
# *e****c*
# *e****c*
# **dddd**DP
#
# Segments are arranged as a,f,g,e,d,c,b,DP
Nums = {'0':[1,1,0,1,1,1,1,0],
        '1':[0,0,0,0,0,1,1,0],
        '2':[1,0,1,1,1,0,1,0],
        '3':[1,0,1,0,1,1,1,0],
        '4':[0,1,1,0,0,1,1,0],
        '5':[1,1,1,0,1,1,0,0],
        '6':[1,1,1,1,1,1,0,0],
        '7':[1,0,0,0,0,1,1,0],
        '8':[1,1,1,1,1,1,1,0],
        '9':[1,1,1,0,1,1,1,0]}

print('Starting ntpclock')
print('The current time is:')
print(time.strftime('%H:%M:%S'))


try:
   while True:
      
      # First timed loop to display the time
   
      TimerDate = (DateTime * 20) - 1
      while TimerDate >=0:

         # Get time and format time string
         Timestr = time.strftime('%H:%M:%S')

         #Form payload
         Data1 = Nums[Timestr[0]] + Nums[Timestr[1]] + Nums[Timestr[3]] + Nums[Timestr[4]] + Nums[Timestr[6]] + Nums[Timestr[7]]

         # Set bits 16 and 32 high to turn on decimal points between hours/minutes and minutes/seconds if the final digit is divisible by 2
         lastSec = int(Timestr[7])
         if lastSec % 2 == 0:
            Data1[15] = 1
            Data1[31] = 1
         else:
            Data1[15] = 0
            Data1[31] = 0

         # Send data to the shift registers
         Shift = 47
         while Shift >= 0:
            GPIO.output(DataPin, GPIO.LOW)

            # Determine if bit is set or clear
            if Data1[Shift] == 1: GPIO.output(DataPin, GPIO.HIGH)

            # Advance the clock
            GPIO.output(ClockPin, GPIO.LOW)
            GPIO.output(ClockPin, GPIO.HIGH)
            Shift -= 1

         # Latch and display the output
         GPIO.output(LatchPin, GPIO.LOW)
         GPIO.output(LatchPin, GPIO.HIGH)

         # Sleep for 50ms
         time.sleep(0.05)

         # Decrement TimerDate
         TimerDate -= 1

      # Second timed loop to display the date
   
      TimerDate = (DateTime * 20) - 1
      while TimerDate >=0:

         # Get date and format date string
         Datestr = time.strftime('%d.%m.%y')

         # Get time and format the time string, only needed for blinking the decimal point
         Timestr = time.strftime('%H:%M:%S')

         #Form payload
         Data1 = Nums[Datestr[0]] + Nums[Datestr[1]] + Nums[Datestr[3]] + Nums[Datestr[4]] + Nums[Datestr[6]] + Nums[Datestr[7]]

         # Set decimal points between day-month and month-year on
         Data1[15] = 1
         Data1[31] = 1

         # Blink last decimal point if the second seconds digit is divisible by 2.
         lastSec = int(Timestr[7])
         if lastSec % 2 == 0:
            Data1[47] = 1
         else:
            Data1[47] = 0

         # Send data to the shift registers
         Shift = 47
         while Shift >= 0:
            GPIO.output(DataPin, GPIO.LOW)

            # Determine if bit is set or clear
            if Data1[Shift] == 1: GPIO.output(DataPin, GPIO.HIGH)

            # Advance the clock
            GPIO.output(ClockPin, GPIO.LOW)
            GPIO.output(ClockPin, GPIO.HIGH)
            Shift -= 1

         # Latch and display the output
         GPIO.output(LatchPin, GPIO.LOW)
         GPIO.output(LatchPin, GPIO.HIGH)

         # Sleep for 50ms
         time.sleep(0.05)

         # Decrement TimerDate
         TimerDate -= 1

except KeyboardInterrupt:
   # Handling of CTRL+C cleanly
   print('Interupted by user, exiting at ')
   print(time.strftime('%H:%M:%S'))

except:
   # Handling any other exceptions
   print('Unknown error occured, exiting at ')
   print(time.strftime('%H:%M:%S'))

finally:
   GPIO.cleanup()  # this ensures a clean exit
