#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    x = my_list[0]
    for i in range(len(my_list) - 1):
        if x < my_list[i]:
            x = my_list[i]
    return x
