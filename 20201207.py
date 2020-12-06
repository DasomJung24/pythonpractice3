"""
Fizzbuzz / 1에서100까지숫자를 출력하는 프로그램. 3으로 나누어 떨어지면 숫자 대신 Fizz를
5로 나누어 떨어지면 숫자 대신 Buzz 를, 3과 5 모두로 나누어 떨어지면 그숫자 대신 FizzBuzz를 출력
"""


def FizzBuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 5 == 0 and num % 3 != 0:
            print('Buzz')
        elif num % 3 == 0 and num % 5 != 0:
            print('Fizz')
        else:
            print(num)

"""
문자열 뒤집기(라이브러리를 쓰지 않고)
"""

def reverse_str(n):
    return n[::-1]

"""
정렬되지 않은 정수 리스트가 주어졌을 때 모든 중복값을 제거한 새로운 리스트를 리턴하는 함수 만들기 
"""

def not_duplicate_list(li):
    return list(set(li))

"""
배낭 문제 
최대 15kg까지 담을 수 있는 배낭이 있고 각각 무게가 다른 짐들이 있다. 1kg 단위로 쪼갤수 있다.
12kg-$4 / 1kg-$2 / 4kg-$10 / 1kg-$1 / 2kg-$2
가격이 최대가 되도록 짐을 고르기 
"""

cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]

def fractional_knapsack(cargo):
    capacity = 15
    pack = []

    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value

"""
주식 사고 팔기. 여러번의 거래로 낼 수 있는 최대의 이익 산출하기 
"""


def maximum_benefit(prices):
    result = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]

    return result