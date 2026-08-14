#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print("{} argument:".format(arguments))
    else:
        print("{} arguments:".format(arguments))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
