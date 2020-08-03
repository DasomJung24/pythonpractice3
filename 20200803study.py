# 2016 년 요일 구하기 a월b일을 입력했을때 요일구하기
def solution(a, b):
    import calendar # calendar 모듈 이용.
    a = calendar.weekday(2016, a, b) # 월0, 화1, 수2, 목3, 금4, 토5, 일6 값 돌려줌.
    if a == 1:
        return 'TUE'
    elif a == 2:
        return 'WED'
    elif a == 3:
        return 'THU'
    elif a == 4:
        return 'FRI'
    elif a == 5:
        return 'SAT'
    elif a == 6:
        return 'SUN'
    else:
        return 'MON'