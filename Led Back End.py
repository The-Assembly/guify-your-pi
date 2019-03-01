from tkinter import *
import RPi.GPIO as GPIO

redPin = 13  #Set to appropriate GPIO
greenPin = 19 #Should be set in the 
bluePin = 26  #GPIO.BOARD format

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
    
def check():
    print(variable)
    if variable.get() == "RED":
        redON()
    else:
        turnOFF()
    
def turnOFF():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)
    
def redON():
    GPIO.output(redPin, GPIO.HIGH)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)
        
