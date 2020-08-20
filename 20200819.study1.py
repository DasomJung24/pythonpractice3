"""
탐색
저장된 정보들 중에서 원하는 값을 찾는 것
선형탐색 - 앞에서부터 순서대로 탐색하는것
이진탐색 - 중간값을 정해 반씩 비교해서 탐색해 가는것. 정렬된 리스트가 아니면 탐색불가.
"""

# 선형탐색 구현.
def linear_search(element, some_list):
    search_number = element
    for i in range(len(some_list)):
        if some_list[i] == search_number:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

# 이진탐색 구현
def binary_search(element, some_list):
    j = 0
    list = some_list
    while len(list) != 0:

        if list[len(list) // 2] == element:
            j += (len(list) // 2)
            return j
        elif list[len(list) // 2] > element:
            list = list[:len(list) // 2]
        elif list[len(list) // 2] < element:
            j += (len(list) // 2) + 1
            list = list[len(list) // 2 + 1:]

        else:
            return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
