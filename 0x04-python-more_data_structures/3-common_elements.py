#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_t = []
    for mot1 in set_1:
        for mot2 in set_2:
            if mot1 == mot2:
                list_t.append(mot1)
    return set(list_t)            
