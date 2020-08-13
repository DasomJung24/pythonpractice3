# 정수리스트 a 의 합.
# def solve(a: list) -> int:
#     result = 0
#     for i in a:
#         result += i
#     return result

#  백준 4673.
# natural_num = set(range(1, 10001))
# generated_num = set()
#
# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)
#
# selfnumber = natural_num - generated_num
#
# for k in sorted(selfnumber):
#     print(k)

# 1부터 1000사이의 한수 구하기.
import sys
#
# num = int(sys.stdin.readline())
# n = 0
#
# for i in range(1, num+1):
#     if i < 100:
#         n += 1
#     else:
#         num_list = list(map(int, str(i)))
#         if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
#             n += 1
# print(n)

# 백준 10809.
# import string
# n = sys.stdin.readline().rstrip()
# asc = list(string.ascii_lowercase)  # 알파벳소문자 순서대로.a-z.
# answer = []
# for i in asc:
#     if i in n:
#         answer.append(str(n.index(i)))
#     else:
#         answer.append('-1')
# print(" ".join(answer))
#
# # 백준 2675.
# num = int(sys.stdin.readline())
#
# for i in range(num):
#     test = list(map(str, sys.stdin.readline().rstrip().split()))
#     test_answer = []
#     for j in range(len(test[1])):
#         test_answer.append(test[1][j] * int(test[0]))
#     print("".join(test_answer))

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a > b:
    print(a)
else:
    print(b)
