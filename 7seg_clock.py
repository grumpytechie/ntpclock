# LED7segTime
# Uses segment strings strung together
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

# Segments definitions for SparkFun Large Digit Driver
Nums = {'0':(1,1,0,1,1,1,1,0),
	'1':(0,0,0,0,0,1,1,0),
	'2':(1,0,1,1,1,0,1,0),
	'3':(1,0,1,0,1,1,1,0),
	'4':(0,1,1,0,0,1,1,0),
	'5':(1,1,1,0,1,1,0,0),
	'6':(1,1,1,1,1,1,0,0),
	'7':(1,0,0,0,0,1,1,0),
	'8':(1,1,1,1,1,1,1,0),
	'9':(1,1,1,0,1,1,1,0)}

print 'the current time is:'
print time.strftime( '%H:%M:%S' )

# main loop
while True:
	tstr=time.strftime( '%S:%M:%S')
	Data1=Nums[tstr[0]]+ Nums[tstr[1]]+ Nums[tstr[3]]+ Nums[tstr[4]]+ Nums[tstr[6]]+ Nums[tstr[7]]
# Send data to the shift registers
	shift = 47
	while shift >= 0:
		GPIO.output(data, GPIO.LOW)

			# determine if bit is set or clear
	        if Data1[shift] == 1: GPIO.output(data, GPIO.HIGH)

		# advance the clock
		GPIO.output(clock, GPIO.LOW)
		GPIO.output(clock, GPIO.HIGH)
		shift=shift-1

	# Latch and display the output
	GPIO.output(latch, GPIO.LOW)
	GPIO.output(latch, GPIO.HIGH)
	time.sleep(.1)
	print tstr
# end
