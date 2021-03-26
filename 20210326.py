"""
프로그래머스 1단계 - 폰켓몬
"""


def solution(nums):
    return min(len(nums)//2, len(set(nums)))


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))