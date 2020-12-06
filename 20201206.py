"""
0보다 크거나 같은 정수 n 이 주어진다. 이때 n! 를 출력하는 프로그램을 작성 하시오 - 재귀사용
"""


def multi(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * multi(n-1)


"""
n번째 피보나치 수 구하는 프로그램
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

