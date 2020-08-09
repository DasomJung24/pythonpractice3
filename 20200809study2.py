# 다섯자리 정수 1개 입력. 각자리수를 분리해 한줄에 하나씩 []에 넣어 출력.
'''
a = list(map(int, input('입력:')))

for i in range(len(a)):
    print([a[i] * (10 ** (4 - i))])
'''

# 시:분:초 입력시 분만 출력.
'''
a = input()
print(int(a[-5:-3]))
'''

# 년.월.일 을 일-월-년 으로 출력.
'''
a = input().split('.')
a.reverse()
print('-'.join(a))
'''
# 실수 입력받아 첫줄에 정수부분 둘째줄에 실수부분 출력.
'''
a = input()
b = a.split('.')
print(b[0],b[1],sep='\n')
'''
# 영어단어를 입력받아 한줄에 한개씩 ''로 묶어 출력.
'''
a = list(input())
for i in a:
    print("'"+i+"'")
'''
# 소수점 11자리까지 반올림 출력.
'''
a = float(input())
print("%0.11f" % a)
'''
# 10진수 입력받아 8진수 출력.
'''
a = int(input())
print(format(a, 'o'))
'''
# 8진수 입력받아 10진수로 출력.
'''
a = input()
b = '0o'+ a
print(int(b, 8))
'''
# 16진수 입력받아 8진수로 출력.
'''
a = input()
b = int('0x'+a, 16)
print(format(b, 'o'))
'''
# 영문자 1개 입력받아 아스키코드의 10진수값으로 출력.
'''
a = input()
print(ord(a))
'''
# 정수 입력받아 아스키 문자로 출력.
'''
a = int(input())
print(chr(a))
'''
# 두개의 정수를 공백으로 구분하여 입력하여 합을 출력.
'''
a, b = map(int, input().split(' '))
print(a+b)
'''
# 입력된 정수의 부호를 바꿔 출력.
'''
a = int(input())
print(-a)
'''
# 영문자 1개 입력받아 그 다음문자 출력.
# 'A' 다음문자는 'B', '0'다음문자는 '1'
'''
a = input()
print(chr(ord(a)+1))
'''
# 정수 2개 공백구분하여 입력하여 나눈 몫 출력.
'''
a, b = map(int, input().split(' '))
print(a // b)
'''
# 정수 2개 공백구분으로 입력. 합,차,곱,몫,나머지,나눈값(소수점둘째자리까지 반올림) 한줄씩 출력.
'''
a, b = map(int, input().split(' '))
print(a+b, a-b, a*b, a//b, a%b, "%0.2f"%(a/b), sep='\n')
'''
# 정수 3개 공백두고 입력. 합과 평균(반올림해서 소수점첫째자리까지) 한줄씩 출력.
'''
a, b, c = map(int, input().split(' '))
sum = a + b + c
print(sum, "%0.1f"%(sum/3), sep='\n')
'''
# 16진수 구구단 출력.
'''
x = input()
y = int(x, 16)
for i in range(1, 16):
    a = format(y*i, 'X')
    b = format(i, 'X')
    print(x+'*'+b+'='+a)
'''
# 369 게임. 1부터 9까지 공백두고 출력. 3,6,9대신 영문대문자 X출력.
a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        print('X', end=' ')
    else:
        print(i, end=' ')