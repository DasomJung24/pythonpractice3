
def is_palindrome(x):
    n = 0
    for i in range(len(x) // 2):
        if x[n] != x[-(n+1)]:
            return False
    return True

a = input('문자를 입력하세요 :')
print(is_palindrome(a))

