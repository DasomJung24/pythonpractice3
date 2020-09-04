# def get_len_of_str(string):
#     new_str = ''
#     for i in range(len(string)):
#         if string[i] not in new_str:
#             new_str += string[i]
#         else:
#             get_len_of_str(string[i:])
#
#     return new_str


#
# def get_len_of_str(string):
#     first_str = ''
#     second_str = ''
#     for i in range(len(string)):
#         if string[i] not in first_str:
#             first_str += string[i]
#         else:
#             break
#
#     for j in range(len(first_str), len(string)):
#         if string[j] not in second_str:
#             second_str += string[j]
#         else:
#             break
#
#     if len(second_str) >= len(first_str):
#         return len(second_str)
#     else:
#         return len(first_str)

#
# def get_len_of_str(string):
#     first_str = ''
#     first_list = []
#     for i in range(len(string)):
#         if string[i] not in first_str:
#             first_str += string[i]
#         else:
#             first_list.append(first_str)
#             get_len_of_str(string[i:])
#             break
#     test_list = []
#     for j in first_list:
#         if len(j) > len(test_list):
#             test_list = j
#     return test_list
#
#
#
# print(get_len_of_str('abcabcabc'))
# print(get_len_of_str(('aaaaa')))
# print(get_len_of_str(('sttrg')))

def same_reverse(num):
    return True if str(num) == str(num)[::-1] else False


print(same_reverse(123))
print(same_reverse(1221))
print(same_reverse(-121))
print(same_reverse(10))