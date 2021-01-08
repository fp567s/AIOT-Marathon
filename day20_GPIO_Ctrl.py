#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!usr/bin/env python
# -*- coding: utf-8 -*-


import RPi.GPIO
import time
from flask import Flask

#RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(18, RPi.GPIO.OUT)
RPi.GPIO.output(18,True)


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/start')
def start():
	#RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setmode(RPi.GPIO.BOARD)
	RPi.GPIO.setup(18,RPi.GPIO.OUT)
	RPi.GPIO.output(18,True)
	#pwm=RPi.GPIO.PWM(12,100)
	#pwm.start(0)
	#while(True):
	#	print('start')
	#	for duty in range(0,100,1):
	#		pwm.ChangeDutyCycle(4)
	#		time.sleep(0.01)
	#		print('Cycle{}'.format(duty))
	return 'start fan control'

@app.route('/stop')
def stop():
	#RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setmode(RPi.GPIO.BOARD)
	RPi.GPIO.setup(18,RPi.GPIO.OUT)
	RPi.GPIO.output(18,False)

	return 'stop fan control'

RPi.GPIO.cleanup()

if __name__ == '__main__':
	app.run(host='192.168.100.2', port=8080, debug=True, threaded=True) #在瀏覽器輸入樹莓派ip,即可

