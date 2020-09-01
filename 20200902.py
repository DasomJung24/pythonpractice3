# 하샤드 수.
# def solution(x):
#     a = []
#     for i in str(x):
#         a.append(i)
#
#     if x % sum(a) == 0:
#         return True
#     else:
#         return False

# 콜라츠 추측.
# def solution(num):
#     if num == 1:
#         return 0
#     count = 1
#     while num > 1:
#         if count == 501:
#             return -1
#         if num % 2 == 0:
#             num = num / 2
#             if num == 1:
#                 return count
#             count += 1
#         else:
#             num = num * 3 + 1
#             count += 1

# n, m 이 한줄에 공백으로 주어지고 *를 이용해 가로길이 n 세로길이 m 인 직사각형 형태 출력.
# a, b = map(int, input().strip().split(' '))
#
# for i in range(b):
#     print(a * '*')

# 정수x, 자연수n / x부터 시작해 x 씩 증가하는 숫자를 n 개 지닌 리스트 리턴.
# def solution(x, n):
#     a = []
#     b = 0
#     for i in range(n):
#         b += x
#         a.append(x)
#     return a
#

def solution(s):
    s1 = s.split(' ')
    new_s = ''
    for i in s1:
        for i, spell in enumerate(i):
            new_s += spell.upper() if i % 2 == 0 else spell.lower()
        new_s += ' '
    return new_s[:-1]


x = 'try hello world'

print(solution(x))
