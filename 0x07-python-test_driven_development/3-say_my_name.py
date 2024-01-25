#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        Prints a name

        args:
            first_name: The first name will be printed
            last_name: The second name to be printed
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)