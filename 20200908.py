# 숫자중 과반수가 넘는 숫자 반환

def more_than_half(nums):

    for num in nums:
        if nums.count(num) >= len(nums)//2:
            return num


print(more_than_half([1, 2, 3, 2, 2, 2, 2]))
print(more_than_half([1,5,2,6,3,4,4,4,4,4,4,4]))
print(more_than_half([2,2,5,1,2,2,1,1,2]))