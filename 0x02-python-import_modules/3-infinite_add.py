#!/usr/bin/python3
#Trevor <Trevor.vaizelstudio@gamail.com>
import sys

def inf_add():
    sum = 0
    i = 1
    argc = len(sys.argv)
    while i < argc:
        sum = sum + int(sys.argv[i])
        i += 1
    print("{}".format(sum))

if __name__ == "__main__":
    inf_add()
