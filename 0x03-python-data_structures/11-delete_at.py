#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        list_P = []
        for i in range(len(my_list)):
            i != idx:
                list_P.append(my_list[i])
        return list_P        

