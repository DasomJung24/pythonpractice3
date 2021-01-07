"""
프로그래머스 2단계 - H-index
"""


# def solution(citations):
#     n = len(citations) - 1
#     result = []
#     while n > 0:
#         if n == len(list(filter(lambda x: x >= n, citations)))\
#                 and len(citations) - n <= len(list(filter(lambda x: x <= n, citations))):
#             result.append(n)
#         n -= 1
#
#     return max(result)

def solution(citations):
    citations.sort(reverse=True)
    count = 0
    for i in citations:
        if i > count:
            count += 1
    return count



print(solution([3, 0, 6, 1, 5]))
