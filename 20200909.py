
def is_valid(string):
    list_1 = []
    list_2 = []
    list_3 = []
    if len(string) == 1:
        return False

    for i in range(len(string)):
        if string[i] == '(':
            if (string[i+1] != ')' and string[i+1] != '(') or string[i] == string[-1]:
                return False
            list_1.append(i)
        if string[i] == ')':
            if list_1:
                list_1.pop()
            else:
                return False
        if string[i] == '[':
            if (string[i+1] != ']' and string[i+1] != '[') or string[i] == string[-1]:
                return False
            list_2.append(i)
        if string[i] == ']':
            if list_2:
                list_2.pop()
            else:
                return False
        if string[i] == '{':
            if (string[i+1] != '}' and string[i+1] != ']') or string[i] == string[-1]:
                return False
            list_3.append(i)
        if string[i] == '}':
            if list_3:
                list_3.pop()
            else:
                return False

    if list_1 == [] and list_2 == [] and list_3 == []:
        return True
    else:
        return False

print(is_valid('()'))
print(is_valid('(){}[]'))
print(is_valid('([)]'))
print(is_valid('{])'))