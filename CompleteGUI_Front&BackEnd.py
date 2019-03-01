from tkinter import *
from PIL import ImageTk, Image
import Adafruit_DHT
import time, sys
import RPi.GPIO as GPIO

redPin = 13  #Set to appropriate GPIO
greenPin = 19 #Should be set in the 
bluePin = 26  #GPIO.BOARD format

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def raise_frame(frame,oldframe):
    oldframe.pack_forget()
    frame.tkraise()
    frame.pack()

def main_frame(frame,oldframe):
    frame.pack_forget()
    oldframe.tkraise()
    oldframe.pack()
    
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
    
def changeAngle(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    
        
root = Tk()
root.title("RPi Jam")

root.geometry("400x300") 
root.resizable(0, 0)

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

path = '/home/pi/Desktop/Pi Jam/RPi.png'
pil_img = Image.open(path)
pil_img = pil_img.resize((150, 200), Image.ANTIALIAS)   

img = ImageTk.PhotoImage(pil_img)
backgroundLogo = Label(topframe, image = img)
backgroundLogo.pack(side = LEFT)

LedButton = Button(bottomframe, text='LED Control', font='Modern 12', bg='lightskyblue', height=3 ,command=lambda:raise_frame(f1,bottomframe)).pack(side=LEFT)
LedBack = Button(f1, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f1,bottomframe)).pack(side=BOTTOM)
variable = StringVar(root)
variable.set("RED")
w = OptionMenu(f1, variable,"RED", "GREEN", "YELLOW","BLUE").pack(side=LEFT)
OnButton = Button(f1, text='ON', font='Modern 8', bg='lightskyblue', height=3 ,command=lambda:check()).pack(side=RIGHT)
OffButton = Button(f1, text='OFF', font='Modern 8', bg='lightskyblue', height=3 ,command=lambda:turnOFF()).pack(side=RIGHT)


SensorButton = Button(bottomframe, text='Sensor Readings', font='Modern 12', bg='lightskyblue', height=3,command=lambda:raise_frame(f2,bottomframe)).pack(side=LEFT)
sensor = Adafruit_DHT.DHT11
pin = 21
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temp = Label(f2, font='Modern 18', text="Temperature: "+str(temperature)+" C").pack(side=TOP)
hum = Label(f2, font='Modern 18', text="Humidity: "+str(humidity)+" %").pack(side=TOP)
SensorBack = Button(f2, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f2,bottomframe)).pack(side=BOTTOM)

motorPin = 20
GPIO.setup(motorPin, GPIO.OUT)
p = GPIO.PWM(motorPin, 100)
p.start(2.5)

MotorButton = Button(bottomframe, text='Motor Control', font='Modern 12', bg='lightskyblue', height=3,command=lambda:raise_frame(f3,bottomframe)).pack(side=LEFT)
slider = Scale(f3, orient = HORIZONTAL, length = 400, width = 20, command=lambda:changeAngle(angle)).pack(side=TOP)
MotorBack = Button(f3, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f3,bottomframe)).pack(side=BOTTOM)

root.mainloop()
