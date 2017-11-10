# amptest
# Turns on all segments to test max current draw of display
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin definitions for shift registers
clock=27
data=17
latch=22

GPIO.setup(data, GPIO.OUT) # Serial Data Line
GPIO.setup(clock, GPIO.OUT) # Clock Line
GPIO.setup(latch, GPIO.OUT) # Latch Line

# Drive pins low initially
GPIO.output(data,GPIO.LOW)
GPIO.output(clock,GPIO.LOW)
GPIO.output(latch,GPIO.LOW)

# Turn on all segments on the 6 digit display
Data1 = [1,1,1,1,1,1,1,1] * 6


print 'Initializing current draw test!'


# main loop
while True:

# Send data to the shift registers
	shift = 47
	while shift >= 0:
		GPIO.output(data, GPIO.LOW)

			# determine if bit is set or clear
	        if Data1[shift] == 1: GPIO.output(data, GPIO.HIGH)

		# advance the clock
		GPIO.output(clock, GPIO.LOW)
		GPIO.output(clock, GPIO.HIGH)
		shift -= 1

	# Latch and display the output
	GPIO.output(latch, GPIO.LOW)
	GPIO.output(latch, GPIO.HIGH)
	time.sleep(.1)
# end

