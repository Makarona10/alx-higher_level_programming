#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except (ZeroDivisionError, ValueError):
        None
    finally:
        if r:
            print("Inside result: {}".format(r))
        return "{}".format(r)
