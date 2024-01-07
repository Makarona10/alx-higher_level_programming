#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    mlis = []
    for i in my_list:
        if (i % 2) == 0:
            mlis.append(True)
        else:
            mlis.append(False)
    return mlis
