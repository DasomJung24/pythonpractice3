"""
프로그래머스 2단계 - 전화번호 목록
"""


def solution(phone_book):
    a = []
    phone_book.sort()
    for i in range(len(phone_book)):
        if not a:
            a.append(phone_book[i])
        else:
            if a[-1] != phone_book[i][:len(a[-1])]:
                phone_book.append(a[-1])
            else:
                return 'false'
    return 'true'


print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))