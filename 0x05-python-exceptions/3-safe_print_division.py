#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        pass
    finally:
        if r != None:
            print("Inside result: {}".format(r))
        return r
