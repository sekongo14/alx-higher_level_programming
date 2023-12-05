#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    else:
        maxs = my_list[0]
        for i in range(a):
            if my_list[i] > maxs:
                maxs = my_list[i]
    return maxs            
