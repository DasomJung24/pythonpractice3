# 입력받은 연,월,일을 yyyy.mm.dd 형식으로 출력.
'''
# 숫자방식
a, b, c = map(int, input().split('.'))

print("%04d"%a, end='.')
print("%02d"%b, end='.')
print("%02d"%c)
'''
# 문자열 메서드 방
'''
a, b, c = map(str, input().split('.'))
print(a.zfill(4)+'.'+b.zfill(2)+'.'+c.zfill(2))
'''
import sys

# 문자열 리스트로 반환.
# a = [sys.stdin.readline().rstrip() for i in range(3)]
# rstrip() 개행문자 출력안되게.

# a, b = map(int, sys.stdin.readline().split())
# print(a,b)
# a+b 한줄에 하나씩 입력받아 출
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)
# # 오른쪽 정렬하여 별찍기.
# n = int(sys.stdin.readline())
# for i in range(1, n+1):
#     print(('*'*i).rjust(n))


