#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    longe = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            longe += 1
        except (IndexError, TypeError, ValueError):
            pass
    print()
    return longe
