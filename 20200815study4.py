"""
스택 Stack
LIFO : Last-in-first-out
가장 마지막에 들어온 데이터가 가장 먼저 삭제된다
데이터간 순서관계를 유지할 수 있다
맨뒤 데이터 추가, 맨뒤데이터 삭제, 맨뒤 데이터 접근.
파이썬에는 스택의 이름을 갖는 자료형은없다. 큐를 이용할 때와 같이 데크를 이용한다.

동적배열과 링크드 리스트를 이용해서 구현할 수 잇다.
출력결과나 시간 복잡도는 같다. -> O(1)
"""

from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append('E')
stack.append('s')
stack.append('w')
stack.append('q')
stack.append('t')

print(stack)

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# 스택을 이용해 괄호 짝이 맞는지 확인하기


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque()  # 사용할 스택 정의

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        if string[i] == ')':
            if stack:
                stack.pop()
            else:
                print(f'문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다.')
    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)