#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    x = list(a_dictionary.keys())[0]
    i = a_dictionary[x]
    for a, b in a_dictionary.items():
        if b > i:
            i = b
            x = a
    return (x)
