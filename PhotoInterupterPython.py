import analogio
import time
import board

photocell = analogio.AnalogIn(board.A2)

counter = 0

while True:
    photo = photocell.value
    print(photo)
    time.sleep(1)
    if photo <= 250:
        counter = counter + 1
    print(counter)
