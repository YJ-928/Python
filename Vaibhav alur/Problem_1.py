# Find PI, exp to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

import math
import numpy as np

def pi(n):
    return format((22/7), f'.{n}f')

def expo(n):
    return round(math.exp(1), n)

x = pi(100)
y = expo(4)

print(x)
print(y)