# 문자열 s를 큰것부터 작은 순으로 정렬. 대문자는 소문자보다 작은 순서로.

def solution(s):
    a = sorted(list(s))
    a.reverse()
    b = ''.join(a)
    return b


s = 'sajfasogZWAfja'
print(solution(s))