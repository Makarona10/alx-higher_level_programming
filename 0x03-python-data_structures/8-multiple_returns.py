#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    res = (len(sentence), sentence[0])
    return res
