"""
프로그래머스 1단계 - 예산
"""


def solution(d, budget):
    price_list = []
    d = sorted(d)
    for price in d:
        if budget - price >= 0:
            budget -= price
            price_list.append(price)
    return len(price_list)


print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))


"""
프로그래머스 1단계 카카오 - 다트게임 
"""


def solution(dartResult):
    score = [str(i) for i in range(1, 11)]
    score_dict = dict()
    for i in score:
        score_dict[i+'S'] = int(i)
        score_dict[i+'D'] = int(i) * int(i)
        score_dict[i+'T'] = int(i) * int(i) * int(i)
    result_list = [0]
    result = 0
    for i in range(len(dartResult)-1):
        print(result_list)
        print(result)
        if dartResult[i:i+2] in score_dict:
            result_list.append(score_dict[dartResult[i:i+2]])
            if len(dartResult) - i > 3:
                if dartResult[i+2] == '*':
                    result += result_list[-1] * 2 + result_list[-2] * 2
                elif dartResult[i+2] == '#':
                    result += result_list[-1] * (-1) + result_list[-2]
            else:
                result += score_dict[dartResult[i:i+2]]
        elif dartResult[i:i+3] in score_dict:
            result_list.append(score_dict[dartResult[i:i+3]])
            if len(dartResult) - i > 3:
                if dartResult[i+2] == '*':
                    result += result_list[-1] * 2 + result_list[-2] * 2
                elif dartResult[i+2] == '#':
                    result += result_list[-1] * (-1) + result_list[-2]
            else:
                result += score_dict[dartResult[i:i+3]]
    return result




print(solution('1D2S0T')
