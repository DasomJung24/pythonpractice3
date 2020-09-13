'''
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
'''
# def remove_min(arr):
#     if len(arr) <= 1:
#         return [-1]
#     arr.remove(min(arr))
#     return arr
#
# print(remove_min([4,3,2,1]))
# print(remove_min([3,6,2,5]))
# print(remove_min([10]))
"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
"""
# def solution(n):
#     n_list = [i for i in str(n)]
#     n_list.sort(reverse=True)
#     return ''.join(n_list)
#
# print(solution(118372))
'''
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
'''
# def solution(n):
#     n_list = [int(i) for i in str(n)]
#     n_list.reverse()
#     return n_list
#
# print(solution(12345))
# print(solution(38295))
'''
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 
배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''
# def solution(array, commands):
#     answer = []
#     for one_list in commands:
#         new_array = array[one_list[0]-1:one_list[1]]
#         new_array.sort()
#         answer.append(new_array[one_list[2]-1])
#     return answer
