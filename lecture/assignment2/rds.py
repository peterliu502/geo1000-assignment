# GEO1000 - Assignment 2
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501

import string

def sentence_value(sentence):
    sentence_value = 0
    sentence_low = sentence.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    for elm in sentence_low:
        if elm in letters:
            sentence_value += letters.index(elm) + 1
    return str(sentence_value)


def rds(value):
    sum = 0
    if len(value) == 1 and value.isdigit():
        return value
    else:
        for elm in value:
            sum += int(elm)
        return rds(str(sum))


if __name__ == "__main__":
    initial_integer = sentence_value("Geomatics is fun!")
    result = rds(initial_integer)
    print(result)
