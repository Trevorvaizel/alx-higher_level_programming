#!/usr/bin/python3
def islower(c):
    if ord(c) not in range(97, 123):
        return False
    else:
        return True

def uppercase(str):
    strlen = len(str) + 1
    for i in range(0, strlen):
        if islower(i):
            i = chr((ord(i) - 32))
        else:
            pass 
