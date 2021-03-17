"""
프로그래머스 2단계 - 다리를 지나는 트럭 
"""


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return time


s = solution(2, 10, [7, 4, 5, 6])
print(s)