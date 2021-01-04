"""
프로그래머스 2단계 - 위장
"""
from itertools import combinations


def solution(clothes):
    clothes_count = dict()
    for cloth in clothes:
        if cloth[1] in clothes_count:
            clothes_count[cloth[1]] += 1
        else:
            clothes_count[cloth[1]] = 2

    result = 1
    for count in clothes_count.values():
        result *= count

    return result - 1



print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))