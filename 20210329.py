"""
프로그래머스 2단계 - 더 맵게
"""
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        elif scoville[0] < K:
            first_min = heapq.heappop(scoville)
            second_min = heapq.heappop(scoville)
            heapq.heappush(scoville, first_min + second_min * 2)
            count += 1
        else:
            break
    return count



# print(solution([1,2,3,9,10,12], 7))
print(solution([6,3,4,15,13], 100))