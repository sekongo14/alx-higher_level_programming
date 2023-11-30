#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    lene = len(sys.argv) - 1
    if lene == 1:
        print("{:d} argument:".format(lene))
    elif lene == 0:
        print("{:d} arguments.".format(lene))
    else:
        print("{:d} arguments:".format(lene))
    for i in range(1, lene+1):
        print("{:d}: {}".format(i, sys.argv[i]))
