import board
import touchio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3F), num_rows=2, num_cols=16)
touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

touchCounter1 = 0
touchCounter2 = 0

while True:
    lcd.set_cursor_pos(0,0)
    lcd.print(str(touchCounter1))
    lcd.set_cursor_pos(1,0)
    lcd.print(str(touchCounter2))
    if touch_A1.value:
        print("Touched A1!")
        touchCounter1 = touchCounter1 + 1
    time.sleep(0.05)
    if touch_A5.value:
        print("Touched A5!")
        touchCounter2 = touchCounter2 + 1
        time.sleep(0.05)
