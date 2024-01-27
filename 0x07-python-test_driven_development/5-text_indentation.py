#!/usr/bin/python3
"""text indentation module"""



def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :

        args:
            text: The text that will be printed
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    newLine = False
    for i in text:
        if newLine == True and text[idx + 1] == " ":
            newLine = False
            continue
        if i == '?' or i == ':' or i == '.':
            print("\n")
            idx = text.index(i)
            newLine = True
        else:
            print(i, end="")