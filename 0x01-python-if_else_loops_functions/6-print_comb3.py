#!/usr/bin/python3
for i in range(48, 58):
    for j in range(48, 58):
        print('{}{}'.format(chr(i), chr(j)), end=", ")
print('{:d}'.format(89))
