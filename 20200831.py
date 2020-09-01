
# def two_sum(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)-i):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#




def reverse(x):
    if x >= 0:
        return int(str(x)[::-1])
    else:
        a = str(x)[0]
        b = int(str(x)[1:][::-1])
        return int(a+str(b))

print(reverse(-3920))


def reverse(x):
  num = str(x)
  remove = "-"
  none = "0"
  if remove in num :
    a = num.strip('-')
    if none in a:
      b = a.strip('')
      return int(remove+b[::-1])
    else :
      return int(remove+a)
  else :
    return int(num[::-1])
print(reverse(0))