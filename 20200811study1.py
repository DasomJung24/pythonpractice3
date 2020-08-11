# 백준 1110 더하기 사이클.
# a = int(sys.stdin.readline())
# count = 0
# num = a
# temp = 0
# newnum = 0
# while True:
#     temp = num // 10 + num % 10
#     newnum = str(num % 10) + str(temp % 10)
#     num = int(newnum)
#     count += 1
#     if a == num:
#         print(count)
#         break
import sys

#
# a = [int(sys.stdin.readline().rstrip()) for i in range(5)]
# sum, avg = 0, 0
# for i in a:
#     if i < 40:
#         i = 40
#     sum += i
# print(sum//5)

# burger = [int(sys.stdin.readline().rstrip()) for i in range(3)]
# soda = [int(sys.stdin.readline().rstrip()) for i in range(2)]
# print(min(burger) + min(soda) - 50)

# 입력한 세수의 중간값 구하기.
# a = list(map(int, sys.stdin.readline().split()))
# a.sort()
# print(a[1])

# 별찍기 응용.
# n = int(sys.stdin.readline())
#
# for i in range(1, n + 1):
#     print('*' * i)
# for j in range(n - 1, 0, -1):
#     print('*' * j)

# 별찍기 응용2.
# n = int(sys.stdin.readline())
#
# for i in range(2 * n - 1, 0, -2):
#     print(('*' * i).center(2*n-1))
# for j in range(3, 2 * n, 2):
#     print(('*' * j).center(2*n-1))
#
# b = n
# for i in range(1, n + 1):
#     print(' ' * (i - 1) + '*' * (2 * (b - i) + 1))
# for j in range(1, b):
#     print(' ' * (b - j - 1) + '*' * (2 * j + 1))
#
# 별찍기 응용3.
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     if n == 1:
#         print('*')
#         break
#     if n % 2 == 1:
#         print(('* ' * (n // 2 + 1)))
#         print(' *' * (n // 2))
#     else:
#         print('* ' * (n // 2))
#         print(' *' * (n // 2))
