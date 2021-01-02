"""
프로그래머스 2단계 - 기능개발
"""


def solution(progresses, speeds):
    days = [(100 - progress) // speed if (100 - progress) % speed == 0 else (100 - progress) // speed + 1
            for progress, speed in zip(progresses, speeds)]
    answer = [[1, days[0]]]
    for i in range(1, len(days)):
        if days[i] <= answer[-1][1]:
            answer[-1][0] += 1
        else:
            answer.append([1, days[i]])

    return [i[0] for i in answer]


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))