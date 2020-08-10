# 백준 1110 더하기 사이클.
a = int(sys.stdin.readline())
count = 0
num = a
temp = 0
newnum = 0
while True:
    temp = num // 10 + num % 10
    newnum = str(num % 10) + str(temp % 10)
    num = int(newnum)
    count += 1
    if a == num:
        print(count)
        break