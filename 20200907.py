def roman_to_num(string):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    number = 0

    for roman_word in string:
        number += roman_dict[roman_word]

    if 'IV' in string or 'IX' in string:
        number -= 2

    if 'XL' in string or 'XC' in string:
        number -= 20

    if 'CD' in string or 'CM' in string:
        number -= 200

    return number

print(roman_to_num('DXLIII'))