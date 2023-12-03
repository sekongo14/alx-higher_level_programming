#!/usr/bin/python3
def no_c(my_string):
    copi = ""
    for car in my_string:
        if car not in ("c", "C"):
            copi += car
    return copi
