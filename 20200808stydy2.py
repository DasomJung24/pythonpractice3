# 덧셈하여 타겟을 만들 수 있는 배열의 두숫자 인덱스를 리턴하라.

nums = [2, 7, 11, 15]
target = 9
'''
브루트 포스 방식.
def target_index(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

'''
'''
브루트 포스보다 빠른 방식. in을 이용.
def target_index(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i +1)]
'''
'''
# 딕셔너리를 이용해 시간복잡도를 개선하여 속도가 훨씬 빨라짐.
def target_index(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(num), nums_map[target - num]]
'''
# 위의 소스코드를 더 간결하게 개선. 실행속도는 큰 차이 없음.
def target_index(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] =  i

print(target_index(nums, target))