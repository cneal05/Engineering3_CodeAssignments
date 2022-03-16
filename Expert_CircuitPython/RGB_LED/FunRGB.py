""" This file is the class-based version of making a single LED fade"""
import time
import board
from rgb import RGB  # import the LED class from the rgb module

redLEDPin1 = board.D8
greenLEDPin1 = board.D9
blueLEDPin1 = board.D10
blueLEDPin2 = board.D4
greenLEDPin2 = board.D5
redLEDPin2 = board.D7

full = 65535
half = int(65535 / 2)

myRGBled1 = RGB(redLEDPin1, blueLEDPin1, greenLEDPin1)
myRGBled2 = RGB(redLEDPin2, blueLEDPin2, greenLEDPin2)

while True:
    myRGBled1.blue()
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.red()
    myRGBled2.cyan(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.green()
    myRGBled2.magenta(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.redBlinky()
    myRGBled2.blueBlinky()
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.Rainbow()
    myRGBled2.ReverseRainbow()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)
