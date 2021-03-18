"""
재귀함수를 이용하지 않고 피보나치 수열 만들기
0, 1, 1, 2, 3, 5, 8, 13, 21, 34....
"""


fibonacci1 = []
for i in range(0, 10):
    if i < 2:
        fibonacci1.append(i)
    else:
        fibonacci1.append(fibonacci1[-1]+fibonacci1[-2])

print(fibonacci1)


fibonacci2 = [0, 1]
[fibonacci2.append(fibonacci2[i-1]+fibonacci2[i-2]) for i in range(0, 10) if i >= 2]

print(fibonacci2)


fibonacci3 = [0, 1]
[fibonacci3.append(fibonacci3[-1]+fibonacci3[-2]) for _ in range(0, 8)]

print(fibonacci3)
