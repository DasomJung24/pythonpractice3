def get_prefix(arr):
    result = arr[0]

    for string in arr:
        if len(string) >= len(result):
            a = len(result)
        else:
            a = len(string)
        for j in range(a):
            if string[0] != result[0]:
                return ''
            elif string[j] == result[j]:
                pass
            else:
                result = result[:j]
    return result


strs = ['start', 'stair', 'step']
strs1 = ['start', 'wework', 'today']

print(get_prefix(strs))
print(get_prefix(strs1))
