"""
접두사 구하기
"""


def solution(strs):
    first_word = strs[0]
    for word in strs:
        for i in range(len(first_word)):
            if word[i] != first_word[i]:
                first_word = first_word[:i]
                break
    return first_word


print(solution(['abcaefg', 'abcdefg', 'abcdhfg']))

"""
시간 구하기 
"""


def solution(p, n):
    hour = ''
    if (p[:2] == 'AM' and p[3:5] != '12') or (p[:2] == 'PM' and p[3:5] == '12'):
        hour = int(p[3:5])
    elif p[:2] == 'AM' and p[3:5] == '12':
        hour = 0
    elif p[:2] == 'PM' and p[3:5] != '12':
        hour = int(p[3:5]) + 12
    minute = int(p[6:8])
    second = int(p[9:11]) + n

    if second >= 60:
        minute += second // 60
        second = second % 60
        if minute >= 60:
            hour += minute // 60
            minute = minute % 60
            if hour >= 24:
                hour = hour % 24
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)


print(solution("AM 12:59:59", 1))


"""
중고차 최대 이익 리턴
"""


def solution(prices):
    result = 0
    for i in range(1, len(prices)):
        for j in range(i):
            if result < prices[i] - prices[j]:
                result = prices[i] - prices[j]
    return result if result > 0 else 0


print(solution([3,2,4,8,7]))

