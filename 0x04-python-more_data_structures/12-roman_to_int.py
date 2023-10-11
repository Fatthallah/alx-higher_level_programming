#!/usr/bin/python3
def to_subtract(list_num):
    t_s = 0
    mx_lst = max(list_num)
    for n in list_num:
        if mx_lst > n:
            t_s = t_s + n
    return (mx_lst - t_s)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rooom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lst_kys = list(rooom_n.keys())
    x = 0
    lst_rm = 0
    lst_nm = [0]
    for ss in roman_string:
        for rrr_n in lst_kys:
            if rrr_n == ss:
                if rooom_n.get(ss) <= lst_rm:
                    x += to_subtract(lst_nm)
                    lst_nm = [rooom_n.get(ss)]
                else:
                    lst_nm.append(rooom_n.get(ss))
                lst_rm = rooom_n.get(ss)
    x += to_subtract(lst_nm)
    return (x)
