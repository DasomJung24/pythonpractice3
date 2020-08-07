# 구구단 리스트로 출력하는 함수 만들기.

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(gugu(2))