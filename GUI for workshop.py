'''Presented by The Assembly'''


from tkinter import *
from PIL import ImageTk, Image
#import Adafruit_DHT
import time, sys
#import RPi.GPIO as GPIO

'''
greenPin = 13   #Set to appropriate GPIO
redPin = 19 #Should be set in the 
bluePin = 26  #GPIO.BOARD format

GPIO.setwarnings(False)

motorPin = 20 #GPIO pin for servo motor
GPIO.setmode(GPIO.BCM) #setup code of declaring GPIO
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

GPIO.setup(motorPin, GPIO.OUT)
p = GPIO.PWM(motorPin, 50) #Setting GPIO pin as PWM with 50Hz
p.start(2.5)
'''
#Both raise_frame $ main_frame functions helps in changing the GUI page

def raise_frame(frame,oldframe):
    oldframe.pack_forget() #removes the old frame and brings up new one
    frame.tkraise()
    frame.pack()

def main_frame(frame,oldframe):
    frame.pack_forget() 
    oldframe.tkraise()
    oldframe.pack()
    
    
        
root = Tk() #starts empty GUI
root.title("RPi Jam") #Declares title of GUI

root.geometry("400x300") #specifies size of GUI
root.resizable(0, 0) 

#Declares different frames which will hold the widgets

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

#Below line is for uploading image
'''
path = '' #specifies path of the image
pil_img = Image.open(path)
pil_img = pil_img.resize((150, 200), Image.ANTIALIAS) #resize the image to 150x200 pixels

img = ImageTk.PhotoImage(pil_img)
backgroundLogo = Label(topframe, image = img) #declares the lable widgets which will hold the image
backgroundLogo.pack(side = LEFT)'''

#Declaration of led buttons
LedButton = Button(bottomframe, text='LED Control', font='Modern 12', bg='lightskyblue', height=3 ,command=lambda:raise_frame(f1,bottomframe)).pack(side=LEFT)
LedBack = Button(f1, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f1,bottomframe)).pack(side=BOTTOM)

#declaration of led buttons and setup code of drop down list
variable = StringVar(root)
variable.set("RED")
w = OptionMenu(f1, variable,"RED", "GREEN", "YELLOW","BLUE").pack(side=LEFT)

OnButton = Button(f1, text='ON', font='Modern 8', bg='lightskyblue', height=3 ,command=lambda:check()).pack(side=RIGHT)
OffButton = Button(f1, text='OFF', font='Modern 8', bg='lightskyblue', height=3 ,command=lambda:turnOFF()).pack(side=RIGHT)


SensorButton = Button(bottomframe, text='Sensor Readings', font='Modern 12', bg='lightskyblue', height=3,command=lambda:raise_frame(f2,bottomframe)).pack(side=LEFT)

#Display of humidity & tempearture readings
temp = Label(f2, font='Modern 18', text="Temperature:  C").pack(side=TOP)
hum = Label(f2, font='Modern 18', text="Humidity:  %").pack(side=TOP)
SensorBack = Button(f2, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f2,bottomframe)).pack(side=BOTTOM)


MotorButton = Button(bottomframe, text='Motor Control', font='Modern 12', bg='lightskyblue', height=3,command=lambda:raise_frame(f3,bottomframe)).pack(side=LEFT)

#declaration of slider which controlls servo motor
slider = Scale(f3, orient = HORIZONTAL, length = 400, width = 20).pack(side=TOP)

MotorBack = Button(f3, text='MAIN', font='Modern 12', bg='bisque2', height=3,command=lambda:main_frame(f3,bottomframe)).pack(side=BOTTOM)


root.mainloop() #function to keep the GUI running
GPIO.cleanup() #GPIO function to switch off all GPIO pins of raspberry pi when GUI is closed
