"""
프로그래머스 2단계 - 주식가격
"""
from collections import deque


def solution(prices):
    prices = deque(prices)
    result = [0 for _ in range(len(prices))]
    i = 0
    while prices:
        main_price = prices.popleft()
        for price in prices:
            if main_price <= price:
                result[i] += 1
            else:
                result[i] += 1
                break
        i += 1
    return result


print(solution([1,2,3,2,3]))
print(solution([2,3,1,2,1,5,7]))