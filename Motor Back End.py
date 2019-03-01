from tkinter import *
import time, sys
import RPi.GPIO as GPIO

def changeAngle(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

motorPin = 20
GPIO.setup(motorPin, GPIO.OUT)
p = GPIO.PWM(motorPin, 100)
p.start(2.5)

