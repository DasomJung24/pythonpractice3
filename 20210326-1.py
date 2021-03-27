"""
프로그래머스 2단계 - 구명보트
"""
from collections import deque


def solution(people, limit):
    people.sort()
    count = 0
    people = deque(people)
    while len(people) > 0:
        if len(people) > 1:
            if people[0] + people[-1] > limit:
                people.pop()
            else:
                people.pop()
                people.popleft()
            count += 1
        else:
            count += 1
            break
    print(count)



solution([70,50,80,50], 100)
solution([70,80,50], 100)
