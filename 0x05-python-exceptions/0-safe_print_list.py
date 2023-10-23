#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    shn = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            shn = shn + 1
        except IndexError:
            break
    print("")
    return (shn)

