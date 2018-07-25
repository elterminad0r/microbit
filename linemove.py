from microbit import *

i = 0

while True:
    i += 1
    boat = [[0] * 5] * 5
    boat[i % 5] = [9 - (i % 5)] * 5
    for k in range(5):
        boat[k][i % 5] = 9 - (i % 5)
    boat = Image(":".join("".join(map(str, row)) for row in boat))
    display.show(boat)
    sleep(100)
