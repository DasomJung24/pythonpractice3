def top_k(nums, k):
    count = 1
    num_list = []
    for j in range(len(nums)):
        for i in nums:
            if nums.count(i) == count:
                num_list.append(i)
                nums.remove(i)
        count += 1

    return num_list[::-1][:k]



print(top_k([1,1,1,2,2,3], 2))