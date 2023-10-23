#!/usr/bin/python3

def list_division(shn_1, shn_2, lenxyz):
    xyz = []
    for x in range(0, lenxyz):
        try:
            res = shn_1[x] / shn_2[x]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            xyz.append(res)
    return (xyz)

