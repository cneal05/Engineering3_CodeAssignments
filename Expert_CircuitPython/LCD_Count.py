#Code originally created by Jay Conklin
#Displays a count on the LCD that increases once every time a wire is touched.
#If a different wire is touched it changes it to counting down instead of up, or vice versa.
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import touchio

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)      #Sets up the lcd board and tells code what pins it's in

touch_a5 = board.A5
touch_A5 = touchio.TouchIn(touch_a5)    #Sets up capacitative touch for the counter wire
touch_a0 = board.A0
touch_A0 = touchio.TouchIn(touch_a0)    #Sets up capacitative touch for the up/down wire

count = 0
updown=1

while True:
    if touch_A5.value:
        count+=updown   #If counter wire is touched adds updown variable to the counter number
                        #Updown will be 1 if going up or -1 if going down, so just adding
                        #it to the counter will make it count 1 in the correct direction
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))   #Above section displays direction of counting and new count
        while touch_A5.value:   #Waits until the wire is released to continue
            time.sleep(.01)     #that holding down the wire does not increase the number over and over

    if touch_A0.value:
        updown=-updown          #If direction wire touched changes updown from 1 to -1 or vice versa
        while touch_A0.value:
            time.sleep(.1)
        lcd.clear()
        if updown==1:
            lcd.print("Up: ")
        else:
            lcd.print("Down: ")
        lcd.print(str(count))   #Above section displays the new direction of counting and current count (the count stays the same)
