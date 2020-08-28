# def is_even(num):
#     if num % 2 == 0:
#         return "짝수 입니다."
#     else:
#         return "짝수가 아닙니다."


# def calculate_total(money):
#     return (money * 0.095 + money * 0.15) + money
#
# print(calculate_total(20))
#
# def get_prefix(str):
#     for i in range(len(str)):
#         if str[i] == '-':
#             return str[:i]
#
# print(get_prefix('BTC-KRW'))
#
# def get_find(str, strs):
#     n = 0
#     while n < len(strs):
#         if strs[n] != str:
#             n += 1
#             continue
#         else:
#             return n
#     return -1
#
#
# output = get_find('a', 'I m  hcker')
# print(output)
#

def find_longest_word(li):
    result = ''
    for i in range(len(li)):
        if len(result) < len(li[i]):
            result = li[i]

    return result

print(find_longest_word(['php', 'exercise', 'backend']))
