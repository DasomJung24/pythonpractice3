"""
프로그래머스 2단계 땅따먹기
"""

#
# def solution(land):
#     result = [max(land[0])]
#     for i in range(len(land)-1):
#         if land[i].index(max(land[i])) == land[i+1].index(max(land[i+1])):
#             temp_list = sorted(land[i+1], reverse=True)
#             result.append(temp_list[1])
#         else:
#             result.append(max(land[i+1]))
#     return sum(result)
#
#
# land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
#
# print(solution(land))


def solution(land):
    for i in range(len(land)-1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[-1])

land = [[1,67,2,8],[35,9,2,5],[23,8,9,4]]

print(solution(land))