#!/usr/bin/python3
def multiple_returns(sentence):
    large = len(sentence)
    first_c = ""
    if large > 0:
        first_c = sentence[0]
    else:
        first_c = None

    return (large, first_c)
