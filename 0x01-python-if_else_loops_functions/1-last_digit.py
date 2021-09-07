#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
str1 = "Last digit of"
if num >= 0:
    last_d = num % 10
else:
    last_d = num % -10
if last_d > 5:
    print("{} {} is {} and is greater than 5".format(str1, num, last_d))
elif last_d == 0:
    print("{} {} is {} and is 0".format(str1, num, last_d))
elif last_d < 6 and last_d != 0:
    print("{} {} is {} and is less than 6 and not 0".format(str1, num, last_d))
