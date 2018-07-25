from microbit import *

ITERATIONS = 10
CX, CY = -0.5, 0
RADIUS = 1.4

def mb_iterate(re, im):
    return re ** 2 - im ** 2, 2 * re * im

def escape_val(re, im, iterations):
    zre, zim = re, im
    for i in range(iterations):
        zre, zim = mb_iterate(zre, zim)
        zre, zim = zre + re, zim + im
        if zre ** 2 + zim ** 2 > 2 ** 2:
            return i / iterations
    return 1

im = []

for y in range(5):
    for x in range(5):
        val = escape_val((x - 2) / 2 * RADIUS + CX,
                         (y - 2) / 2 * RADIUS + CY,
                         ITERATIONS)
        im.append(str(int(9 * val)))
    if y != 4:
        im.append(":")


display.show(Image("".join(im)))
