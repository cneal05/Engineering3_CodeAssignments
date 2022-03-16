# These are the libraries needed to fade an LED, even if you imported elsewhere
import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)
lightBulb.direction = digitalio.Direction.OUTPUT


class LED:  # It's propper coding to always write a line explaining a class
    # with a "docstring."   Like this:
    """LED is a class designed for a single color LED to fade in and out"""

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        # start each object with "self.object"
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadeUp(self):
        lightBulb.value = 65535
        for i in range(255):
            if i < (255 / 2):
                self.led.duty_cycle = int(i * 65535 / (255 / 2))

            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeDown(self):
        lightBulb.value = 65535
        for i in range(255):
            if i > (255 / 2):
                self.led.duty_cycle = 65535 - int((i - (255 / 2)) * 65535 / (255 / 2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535

    def off(self):  # "off" means duty cycle should be full.
        self.led.duty_cycle = 65535


class RGB:
    from rgb import LED

    def __init__(self, redPin, bluePin, greenPin):
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def red(self, brightness=65535):
        self.myRedLED.on(brightness)
        self.myBlueLED.off()
        self.myGreenLED.off()

    def blue(self, brightness=65535):
        self.myRedLED.off()
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()

    def green(self, brightness=65535):
        self.myRedLED.off()
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)

    def yellow(self, brightness=65535):
        self.myRedLED.on(brightness)
        self.myBlueLED.off
        self.myGreenLED.on(brightness)

    def cyan(self, brightness=65535):
        self.myRedLED.off()
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)

    def magenta(self, brightness=65535):
        self.myRedLED.on(brightness)
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()

    def off(self):
        self.myRedLED.off()
        self.myBlueLED.off()
        self.myGreenLED.off()
        lightBulb.value = 0

    def redBlinky(self, brightness=65535):
        self.myRedLED.fadeDown()
        time.sleep(0.3)
        self.myRedLED.fadeUp()
        time.sleep(0.3)

    def blueBlinky(self, brightness=65535):
        self.myBlueLED.fadeDown()
        time.sleep(0.3)
        self.myBlueLED.fadeUp()
        time.sleep(0.3)


    def greenBlinky(self, brightness=65535):
        self.myGreenLED.fadeDown()
        time.sleep(0.3)
        self.myGreenLED.fadeUp()
        time.sleep(0.3)

    def Rainbow(self, brightness = 65535):
        self.myRedLED.fadeDown()
        self.myGreenLED.fadeDown()
        self.myRedLED.fadeUp()
        self.myBlueLED.fadeDown()
        self.myGreenLED.fadeUp()
        self.myRedLED.fadeDown()
        self.myBlueLED.fadeUp()
        self.myRedLED.fadeUp()

    def ReverseRainbow(self, brightness = 65535):
        self.myRedLED.fadeDown()
        self.myBlueLED.fadeDown()
        self.myRedLED.fadeUp()
        self.myGreenLED.fadeDown()
        self.myBlueLED.fadeUp()
        self.myRedLED.fadeDown()
        self.myGreenLED.fadeUp()
        self.myRedLED.fadeUp()
        #self.myRedLED.fadeUp()
        #self.myBlueLED.fadeDown()
        #self.myGreenLED.fadeUp()
        #self.myRedLED.fadeDown()
        #self.myBlueLED.fadeUp()
        #self.myRedLED.fadeUp()
