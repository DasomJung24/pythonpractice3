"""
프로그래머스 2단계 - 가장 큰 수
"""
import itertools


def solution(numbers):
    number_list = list(itertools.permutations(numbers, len(numbers)))
    return str(max(''.join([str(i) for i in number]) for number in number_list))



def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), key=lambda x: x*3, reverse=True))))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))