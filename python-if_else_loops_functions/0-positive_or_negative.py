#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    status = "is negative"
elif number > 0:
    status = "is positive"
else:
    status = "is zero"
print(f"{number} {status}")
