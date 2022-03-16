''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import LED   # import the LED class from the rgb module

blueLEDPin1 = board.D10
redLEDPin1 = board.D8
greenLEDPin1 = board.D9

blueLEDPin2 = board.D4
redLEDPin2 = board.D7
greenLEDPin2 = board.D5

myBlueLED1 = LED(blueLEDPin1, "blue1")
myRedLED1 = LED(redLEDPin1, "red1")
myGreenLED1 = LED(greenLEDPin1, "green1")
myBlueLED2 = LED(blueLEDPin2, "blue2")
myRedLED2 = LED(redLEDPin2, "red2")
myGreenLED2 = LED(greenLEDPin2, "green2")

while True:
    myGreenLED1.fadeup()
    myGreenLED2.fadeup()
    #time.sleep(1)
    myBlueLED1.fadeup()
    myBlueLED2.fadeup()
    #time.sleep(1)
    myRedLED1.fadeup()
    myRedLED2.fadeup()
    #time.sleep(1)
    myBlueLED1.fadedown()
    myBlueLED2.fadedown()
    #time.sleep(1)
    myBlueLED1.fadeup()
    myBlueLED2.fadeup()
    #time.sleep(1)
    myRedLED1.fadedown()
    myRedLED2.fadedown()
    #time.sleep(1)
    myRedLED1.fadeup()
    myRedLED2.fadeup()
    #time.sleep(1)
    myGreenLED1.fadedown()
    myGreenLED2.fadedown()
    #time.sleep(1)
