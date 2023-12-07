#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_t = []
    for n in my_list:
        if n not in list_t:
            list_t.append(n)
    return sum(list_t)
