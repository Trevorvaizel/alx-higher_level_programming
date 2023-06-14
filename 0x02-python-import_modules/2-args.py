#!/usr/bin/python3
#Trevor <trevor.vaizel@gmail.com>
import sys

def arg_count():
    argc = len(sys.argv) - 1
    counter = 1

    if argc != 1:
        print("{} arguments:".format(argc))
    else:
        print("{} argument:".format(argc))

    for arg in sys.argv[1:]:
        print("{}: {}".format(counter, arg))
        counter += 1

if __name__ == "__main__":
    arg_count()
