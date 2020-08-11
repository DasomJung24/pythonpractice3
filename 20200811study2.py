# 9개 서로다른 자연수 한줄씩 입력. 최댓값, 최대값이몇번째인지 한줄씩 출력.
import sys

#
# li = [int(sys.stdin.readline().rstrip()) for i in range(9)]
# print(max(li))
# print(li.index(max(li)) + 1)

# 세개의 자연수 한줄씩 입력. 세수를 곱한 값에서 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 각각 한줄씩 출력.
# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# sum = list(str(a * b * c))
#
# for i in range(10):
#     n = sum.count(str(i))
#     print(n)

# 음이 아닌 정수를 한줄씩 10줄에 걸쳐 입력. 42로 나눌때 서로 다른 나머지의 개수 출력.
# li = [int(sys.stdin.readline().rstrip()) for i in range(10)]
# l = []
# for num in li:
#     l.append(num % 42)
#     s = set(l)
# print(len(s))
# 더 간단한 예.
# li = []
# for i in range(10):
#     n = int(input())
#     li.append(n % 42)
# li = set(li)
# print(len(li))

# 과목수, 성적들 입력. 점수/성적최대값*100 새로운점수만듬. 새로운점수의 펑균출력.
# N = int(sys.stdin.readline())
# score = list(map(int, sys.stdin.readline().split()))
# s_max = max(score)
# new_score = []
# for i in range(N):
#     new_score.append(score[i] / s_max * 100)
# print(sum(new_score) / len(new_score))

# 백준 8958.
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     score = list(str(sys.stdin.readline().rstrip()))
#     count = 0
#     arr = []
#     for j in score:
#         if j == 'O':
#             count += 1
#             arr.append(count)
#         else:
#             count = 0
#     print(sum(arr))
# 백준 4344.
# num = int(sys.stdin.readline())
#
# for i in range(num):
#     score = list(map(int, sys.stdin.readline().split()))
#     n = 0
#     avg = sum(score[1:]) / score[0]
#     for k in range(1, len(score)):
#         if score[k] > avg:
#             n += 1
#     print(str("%0.3f" % round(n / score[0] * 100, 3))+'%')
#

print(round(3.25, 1))