"""
카카오 블라인드 채용 - 실패율
"""


def solution(n, stages):
    failure_rate = dict()
    total = len(stages)
    for i in range(1, n+1):
        if total == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = stages.count(i) / total
            total -= stages.count(i)
    sorted_dict = sorted(failure_rate.items(), key=(lambda x: x[1]), reverse=True)
    return [i[0] for i in sorted_dict]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


"""
카카오 블라인드 채용 - 비밀지도 
"""


def solution(n, arr1, arr2):
    arr1 = [list(format(i, 'b').zfill(n)) for i in arr1]
    arr2 = [list(format(i, 'b').zfill(n)) for i in arr2]
    result = []
    for i, j in zip(arr1, arr2):
        res = ''
        for x, y in zip(i, j):
            if x == '0' and y == '0':
                res += ' '
            else:
                res += '#'
        result.append(res)
    return result

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))