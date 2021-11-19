"""
로또 최고순위와 최저순위 구하기 - 프로그래머스 1단계
"""


def solution(lottos, win_nums):
    min: int = 0
    max: int = 0
    for num in win_nums:
        if num in lottos:
            min += 1

    max = min + lottos.count(0)

    return [7-max if max else 6, 7-min if min else 6]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
