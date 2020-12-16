"""
카카오 인턴 - 키패드 누르기
"""

#
# def solution(numbers, hand):
#     key_pad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
#                4: (1, 0), 5: (1, 1), 6: (1, 2),
#                7: (2, 0), 8: (2, 1), 9: (2, 2),
#                '*': (3, 0), 0: (3, 1), '#': (3, 2)}
#     result = ''
#     left_hand = '*'
#     right_hand = '#'
#     for number in numbers:
#         if number in [1, 4, 7]:
#             result += 'L'
#             left_hand = number
#         elif number in [3, 6, 9]:
#             result += 'R'
#             right_hand = number
#         else:
#             left_distance = abs(key_pad[left_hand][0] - key_pad[number][0]) + abs(key_pad[left_hand][1] - key_pad[number][1])
#             right_distance = abs(key_pad[right_hand][0] - key_pad[number][0]) + abs(key_pad[right_hand][1] - key_pad[number][1])
#             if left_distance == right_distance:
#                 if hand == 'left':
#                     result += 'L'
#                     left_hand = number
#                 else:
#                     result += 'R'
#                     right_hand = number
#             elif left_distance > right_distance:
#                 result += 'R'
#                 right_hand = number
#             else:
#                 result += 'L'
#                 left_hand = number
#     return result
#
#
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))


"""
카카오 - 크레인 인형뽑기 
"""


def solution(board, moves):
    box = [0]
    result = 0
    for move in moves:
        for i in board:
            if i[move-1] != 0:
                if box[-1] == i[move-1]:
                    i[move-1] = 0
                    del box[-1]
                    result += 2
                else:
                    box.append(i[move-1])
                    i[move-1] = 0
                break
    return result

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


"""
1단계 - 소수찾기 : 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수 만들기 
"""


def solution(n):
    result = 0
    for i in range(1, n+1):
        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a += 1
        if a == 2:
            result += 1

    return result


print(solution(10))