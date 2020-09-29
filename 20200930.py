'''
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를
배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    li = []
    for i in range(len(numbers)):
        for j in range(-1,-(len(numbers)),-1):
            if i - len(numbers) != j:
                a = numbers[i]+numbers[j]
                li.append(a)
    s = set(li)
    return sorted(list(s))