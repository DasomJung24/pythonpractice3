"""
전체 학생수 n, 체육복 도난당한 학생번호 배열 lost, 여벌의 체육복 가져온 학생 번호 배열 reserve
번호 앞뒤로만 빌려주기 가능. 체육수업을 들을수 있는 학생의 최대값 리턴.
"""


def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

n = 5
lost = [2,4]
reserve = [1,3,5]

print(solution(n, lost, reserve))