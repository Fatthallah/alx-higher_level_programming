#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    y = 0
    for l in my_list:
        x += l[0] * l[1]
        y += l[1]
    return (x / y)

