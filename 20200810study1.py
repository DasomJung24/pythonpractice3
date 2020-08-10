# 3 수가 주어졌을 때 만들수 있는 경우의 수 출력. 총 개수 출력.
'''
r, g, b = map(int, input().split(' '))
sum = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            sum += 1
            print(i, j, k)
print(sum)
'''
# 1부터 입력받은 정수까지 1씩 증가 시켜 한줄에 공백으로 구분 출력. 3의배수는 출력하지않음.
'''
a = int(input())
i = 1

while True:
    if not i % 3 ==0:
        print(i, end=' ')
        i += 1
    else:
        i += 1
        continue
    if i > a:
        break
'''
# 등차수열의 시작값a 등차값d 몇번째수인지의미하는정수n 이 입력될때 n번째 수 출력.
'''
a, d, n = map(int, input().split(' '))
i = 1
while i < n:
    a = a + d
    i += 1
print(a)
'''
# 같은날 동시 가입 인원3명이 규칙적인 방문주기를 갖고있다. 3이 같이 방문하는 날 출력.
'''
a, b, c = map(int, input().split(' '))

day = 1
while (day%a != 0 or day%b != 0 or day%c != 0):
    day += 1
print(day)
'''
# 번호가 불린 횟수 출력. 학생수23.무작위로출석부름.
'''
n = int(input())
num = list(input().split(' '))
arr = []
for i in range(23):
    arr.append(0)

for i in range(len(num)):
    a = int(num[i])
    arr[a-1] += 1

for i in range(len(arr)):
    print(arr[i], end=' ')
'''
# 무작위 숫자중 가장 작은 숫자.
'''
n = int(input())
num = list(map(int, input().split(' ')))

print(min(num))
'''
# 19*19 바둑판에 놓을 바둑돌 n개 첫줄에입력.
# 돌을 놓을 좌표x,y가 n줄 입력. 돌있는 위치 1 없는위치 0 으로 바둑판 출력.
'''
arr = [[0]*19 for i in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

for i in arr:
    i = map(str, i)
    a = " ".join(i)
    print(a)
'''
# 격자판의 세로h 가로w 첫줄.막대개수n둘째줄.각막대의길이l,방향d(가로0세로1),좌표xy.
'''
h, w = map(int, input().split())
arr = [[0 for i in range(w)] for j in range(h)]

for i in range(int(input())):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            arr[x-1][y-1+j] = 1
        else:
            arr[x-1+j][y-1] = 1

for q in arr:
    q = map(str, q)
    a = ' '.join(q)
    print(a)
'''
# 코드업 기본100제중 100번째 문제.
arr = []
for i in range(10):
    temp = list(map(int, input().split()))
    arr.append(temp)

i, j = 1, 1

while True:
    if arr[i][j] == 2:
        arr[i][j] = 9
        break
    arr[i][j] = 9
    j +=1
    if arr[i][j] == 1:
        i += 1
        j -= 1
    if arr[i][j] == 1 and arr[i+1][j-1] == 1:
        break
    if i == 8 and j == 8:
        arr[i][j] = 9
        break


for k in arr:
    k = map(str, k)
    q = ' '.join(k)
    print(q)






