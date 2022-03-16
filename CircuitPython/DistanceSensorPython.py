# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

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
