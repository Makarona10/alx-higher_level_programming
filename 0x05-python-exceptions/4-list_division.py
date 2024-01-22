#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newL= []
    for i in range(len(my_list_1)):
        try:
            newL += [my_list_1[i] / my_list_2[i]]
        except (ValueError, TypeError):
            newL += [0]
        except ZeroDivisionError:
            print("division by 0")
            newL += [0]
        except IndexError:
            print("out of range")
        finally:
            pass
    return newL
