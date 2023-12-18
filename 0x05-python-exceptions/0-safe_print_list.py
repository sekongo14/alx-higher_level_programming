#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    longe = 0
    for y in range(x):
        try:
            print(my_list[y], end="")
            longe += 1
            except IndexError:
                pass
    print()
    return longe
