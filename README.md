# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_UltraSensor](#CircuitPython_UltraSensor)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence
Pictures / Gifs of your work should go here

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://www.markdownguide.org/basic-syntax/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
Create code for that makes a servo sweep between 0 and 180, then add a capacitive touch feature so that when you touch one wire, it will go one way, if you touch the other one, it will go the other way.

```python
import time
import board
import touchio
import pwmio
import servo

pwm = pwmio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

while True:
    if touch_A1.value:
        print("Touched A1!")
        my_servo.angle = 90
    time.sleep(0.05)
    if touch_A2.value:
        print("Touched A2!")
        my_servo.angle = 0
    time.sleep(0.05)
```

### Evidence
 ![CapacitiveTouchServo](/Images/Gifs/ezgif.com-gif-maker.gif)
 
 A gif of the capactive touch servo working
### Wiring
 ![circuitPhoto](/Images/CapaServo.png)
### Reflection
This assignment was not very difficult, which is to be expected, being one of the first assignments of the year. Making the capacitive touch part was a little tricky, but there are many helpful websites on the internet explaining how to do it.

## CircuitPython_UltraSensor

### Description & Code

```python
import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
print("new code")
cm = 0
r = 0
g = 0
b = 0
while True:
    try:
        cm = sonar.distance
        print((cm))
        if cm <= 5:
            r = 255
            g = 0
            b = 0
        elif cm <= 20:
            r = int(255 - ((cm - 5) / 15 * 255))  #
            g = 0
            b = int((cm - 5) / 15 * 255)
        elif cm <= 35:
            r = 0
            g = int((cm - 20) / 15 * 255)
            b = int(255 - ((cm - 20) / 15 * 255))
            print((r, g, b))
        else:
            r = 0
            g = 255
            b = 0
        dot.fill((r, g, b))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence

### Wiring
![UltraSensorWiring](/Images/UltraSensorPhoto.png)
### Reflection





## CircuitPython_PhotoInterupter

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring 

### Reflection
