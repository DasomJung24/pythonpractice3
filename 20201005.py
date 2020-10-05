"""
nums 라는 정렬되지 않은 숫자배열을 주면 선택정렬알고리즘으로 오름차순으로 정렬해서 리턴
"""
nums=[3,2,7,4,9,15,7,3]
# def selectionSort(nums):
#     return sorted(nums)

def selectionSort(nums):
    result = []
    while len(nums) > 0:
        result.append(min(nums))
        nums.pop(nums.index(min(nums)))

    return result
print(selectionSort(nums))

