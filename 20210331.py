"""
프로그래머스 2단계 - 오픈채팅방
"""


def solution(record):
    result = list()
    temp_dict = dict()

    for i in record:
        i = i.split(' ')
        if i[0] == 'Enter' or i[0] == 'Change':
            temp_dict[i[1]] = i[2]

    for i in record:
        i = i.split(' ')
        if i[0] == 'Enter':
            result.append(temp_dict[i[1]] + '님이 들어왔습니다.')
        elif i[0] == 'Leave':
            result.append(temp_dict[i[1]] + '님이 나갔습니다.')
        else:
            pass

    return result


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])