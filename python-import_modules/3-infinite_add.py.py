#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len_argv = len(argv)
    i = 1
    sum = 0
    while i < len_argv:
        sum += int(argv[i])
        i += 1
print("{}".format(sum))
