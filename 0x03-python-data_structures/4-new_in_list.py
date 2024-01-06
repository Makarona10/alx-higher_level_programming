#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = [0] * len(my_list)
    if (my_list[idx] < 0 or idx >= len(my_list)):
        return (my_list)
    for i in range(0, len(my_list)):
        newList[i] = my_list[i]

    newList[idx] = element
    return newList
