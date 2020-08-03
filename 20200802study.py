# 신용(체크)카드번호를 입력받을때 가운데 8자리를 제외하고는 *로 가려지게 작성하세요.(16자리) [2번째 예제 중]
'''
cardNum = input('카드번호를 입력하세요:')

print('*'*4+cardNum[4:-4]+'*'*4)
'''
# 정수 num이 짝수일 경우 'Even'을 반환하고 홀수인 경우 'Odd'를 반환하는 함수, solution을 완성해주세요. 0도 짝수입니다.
"""
def solution(num):
    if num % 2 == 0:
        return 'Even'
    elif num % 2 == 1:
        return 'Odd'
    else:
        return 'Even'

num = int(input('숫자를입력하세요:'))
print(solution(num))
"""
# 모범 답안(?)
"""
def solution(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"
"""
#문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

def solution(s):
    s = int(s)
    return s

s = input('문자열을입력하세요:')
print(s)