#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    r = roman_dict
    s = roman_string
    for i in range(len(roman_string)):
        if i > 0 and r[s[i]] > r[s[i - 1]]:
            num += r[s[i]] - 2 * r[s[i - 1]]
        else:
            num += r[s[i]]
    return num
