#!/usr/bin/python3
#Trevor <trevor.vaizel@gmail.com>

def arg_count(*args):
    argc = len(args)
    counter = 1

    if argc != 1:
        print("{} arguments:".format(argc))
    else:
        print("{} argument:".format(argc))

    for arg in args:
        print("{}: {}".format(counter, args))
        counter += 1

if __name__ == "__main__":
    arg_count()
