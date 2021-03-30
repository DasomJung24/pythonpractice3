"""
프로그래머스 2단계 - 올바른 괄호
"""


def solution(s):
    stack = []
    if s[0] == ')':
        return False
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
    return len(stack) == 0


print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))