#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last_num = num_str[-1]
if last_num > str(5):
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == str(0):
    print(f"Last digit of {number} is {last_num} and is 0")
elif last_num < str(6) and last_num != str(0):
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
