# 팰린드롬인지 확인하기. 단, 띄어쓰기가 포함된 문장. 대소문자를 구분하지 않으며 영문자와 숫자만 대상임.

import collections

def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque() # 리스트보단 데크를 선언해 더 빠른 실행속도.
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

print(isPalindrome('A man, a plan, a canal : Panama'))
print(isPalindrome('race A car'))

# 슬라이싱과 정규식을 이용한 방법.

import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(isPalindrome('A man, a plan, a canal : Panama'))
print(isPalindrome('race A car'))
