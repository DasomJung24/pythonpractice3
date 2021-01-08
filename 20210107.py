"""
프로그래머스 2단계 - 카펫
"""


def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total):
        if (total % i == 0) and (total // i > 2) and (i >= total // i) and ((i - 2) * (total // i - 2) == yellow):
            return [i, total // i]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))