def del_comma(price):
    result = ''
    for i in price:
        if ',' != i:
            result += i
        else:
            pass
    return int(result)

result = del_comma('1,000')
print(type(result))
print(del_comma('1,000'))
print(del_comma('10,000'))
print(del_comma('100,000'))
print(del_comma('1,000,000'))
print(del_comma('10,000,000'))


