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

