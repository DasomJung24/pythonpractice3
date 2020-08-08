# 여러가지 정렬 방법

a = [4, 1, 8, 3, 9]
print(sorted(a))

b = 'fjsao'
print(sorted(b)) # 알파벳 순서대로 정렬한 리스트로 출력
print(''.join(sorted(b))) # 리스트를 문자열로 출력

# a.sort()  # 리스트 자체를 정렬. 입력을 출력으로 덮어 쓰기 때문에 리턴값이 None 이므로 주의.

c = ['ccc', 'aaaaa', 'd', 'bb']
print(sorted(c, key=len))  # key=옵션 지정가능. 길이순서대로 정렬.

d = ['cde', 'cfc', 'abc']

def fn(s):
    return s[0], s[-1]

print(sorted(d))
print(sorted(d, key=fn)) # 두번째 키값을 s[-1]로 비교하게 하는 함수 이용.

print(sorted(d, key=lambda s:(s[0], s[-1])))
