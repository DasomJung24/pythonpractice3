"""
행렬의 덧셈
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution 을 완성해주세요.
"""


def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]

    return arr1


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


"""
2단계 - 프린터 
"""


# 첫번째 방법

import copy


def solution(priorities, location):
    new_list = copy.deepcopy(priorities)
    new_list[location] = 'a'
    print(new_list)
    count = 0
    priorities_length = len(priorities)

    while priorities_length > 0:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            priorities.remove(priorities[0])
            new_list.append(new_list[0])
            new_list.remove(new_list[0])
        else:
            priorities.remove(priorities[0])
            if new_list[0] == 'a':
                return count + 1
            new_list.remove(new_list[0])
            count += 1
            priorities_length -= 1


# 두번째 방법 - 베스트

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

