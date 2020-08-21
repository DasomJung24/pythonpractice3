#
# def merge_and_swap(list1, list2):
#   # 이 함수를 구현해 주세요
#     if list1 == [] and list2 == []:
#         return []
#     else:
#         list1 = list1 + list2
#         list1[0], list1[-1] = list1[-1], list1[0]
#         print(list1)
#
# list1 = [1,2,3,4]
# list2 = [5,6,7]
#
# merge_and_swap(list1, list2)
#
# my_list = ['one', 2, 3, 4, 'three', 'three']
#
# set1 = set()
# for i in range(len(my_list)):
#   for j in range(i+1, len(my_list)):
#     if my_list[i] == my_list[j]:
#       set1.add(i)
#
# set2 = set(my_list) - set1
# list1 = list(set2)
# print(sorted(list1))
#
# def find_smallest_integer_divisor(numb):
#   n = 2
#   while n != numb:
#     if numb % n != 0:
#       n += 1
#       continue
#     elif numb % n == 0:
#       break
#   return n
#
# # print(find_smallest_integer_divisor(15))
#
# def what_is_my_full_name(**kwargs):
#   if 'first_name' in kwargs and 'last_name' in kwargs:
#     return kwargs['last_name']+' '+kwargs['first_name']
#   elif 'first_name' in kwargs:
#     return kwargs['first_name']
#   elif 'last_name' in kwargs:
#     return kwargs['last_name']
#   else:
#     return Nobody
#
# print(what_is_my_full_name(a=3, b=4, c=5, first_name='jane', last_name='han'))


def name_decorator(name):
    def greeting():
        return "Hello, name"

    return greeting


@name_decorator("정우")
def greeting():
    return "Hello, "

greeting()