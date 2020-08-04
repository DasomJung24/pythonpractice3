# 문자열리스트 Seoul이 요소중 Kim의 위치 x찾기.

def solution(arr):
    x = arr.index('Kim')
    return '김서방은 '+str(x)+'에 있다.'

Seoul = ['Jane','Tom','Kim','Lee']

print(solution(Seoul))
