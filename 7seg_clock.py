# ntpclock
#
# A simple Raspberry Pi project that uses shift registers to
# display time on 7-segment displays.
# GrumpyTechie - 2017

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin definitions for shift registers
ClockPin=27
DataPin=17
LatchPin=22

GPIO.setup(DataPin, GPIO.OUT) # Serial Data Line
GPIO.setup(ClockPin, GPIO.OUT) # Clock Line
GPIO.setup(LatchPin, GPIO.OUT) # Latch Line

# Drive pins low initially
GPIO.output(DataPin,GPIO.LOW)
GPIO.output(ClockPin,GPIO.LOW)
GPIO.output(LatchPin,GPIO.LOW)

# Segments definitions for SparkFun Large Digit Driver
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

print ('the current time is:')
print (time.strftime('%H:%M:%S'))

# main loop
while True:

    # First timed loop to shift out current time every tenth of a second with DP off.
    # Timer1 sets the time the DP is on and off, in 100ms increments
    Timer1 = 9
    while Timer1 >= 0:
        Timestr = time.strftime('%H:%M:%S')
        Data1 = Nums[Timestr[0]] + Nums[Timestr[1]] + Nums[Timestr[3]] + Nums[Timestr[4]] + Nums[Timestr[6]] + Nums[Timestr[7]]

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
        time.sleep(.1)
        Timer1 -= 1

    # Second timed loop for 1 sec with decimal points (DP) turned on between hours and minutes, and minutes and seconds
    Timer1 = 9
    while Timer1 >= 0:
        Timestr = time.strftime('%H:%M:%S')
        Data1 = Nums[Timestr[0]] + Nums[Timestr[1]] + Nums[Timestr[3]] + Nums[Timestr[4]] + Nums[Timestr[6]] + Nums[Timestr[7]]

        # Set bits 16 and 32 high to turn on DPs
        Data1[15] = 1
        Data1[31] = 1

        # Send data to the shift registers
        Shift = 47
        while Shift >= 0:
            GPIO.output(DataPin, GPIO.LOW)

            # Determine if bit is high or low
            if Data1[Shift] == 1: GPIO.output(DataPin, GPIO.HIGH)

            # Advance the clock
            GPIO.output(ClockPin, GPIO.LOW)
            GPIO.output(ClockPin, GPIO.HIGH)
            Shift -= 1

        # Latch and display the output
        GPIO.output(LatchPin, GPIO.LOW)
        GPIO.output(LatchPin, GPIO.HIGH)
        time.sleep(.1)
        Timer1 -= 1
