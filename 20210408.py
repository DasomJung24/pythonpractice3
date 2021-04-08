"""
프로그래머스 2단계 - 피보나치 수
"""


def solution(n):
    fibo = list()
    for i in range(n+1):
        if i < 2:
            fibo.append(i)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    print(fibo[-1]%1234567)



solution(5)
