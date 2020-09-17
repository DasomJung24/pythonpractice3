# def reverseString(s):
#     result = []
#     for i in range(-1, -(len(s)+1), -1):
#         result.append(s[i])
#     return result
#
# print(reverseString(['g','d','r','q','c']))
#
# for i in range()

input_list = [0, 1, 0, 3, 12]

def moveZeroes(nums):
    count = 0
    while 0 in nums:
        if 0 in nums:
            nums.remove(0)
            count += 1
    for add in range(count):
        nums.append(0)

    return nums

print(moveZeroes(input_list))

