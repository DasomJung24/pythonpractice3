"""
다음과 같이 비밀번호의 길이와 대문자가 포함된것을 확인하는 간단한 함수가 있습니다.
"""


# def check_password(password):
#     if len(password) < 8:
#         return 'SHORT_PASSWORD'
#
#     if not any(c.isupper() for c in password):
#         return 'NO_CAPITAL_LETTER_PASSWORD'
#
#     return True
#
#
# password = 'Risjodsjaga'
# print(check_password(password))
#
# 이함수에 있는 if문 두개를 람다표현식을 이용하여 다음과 같은 형식으로 작성해 보세요.
#
# 아래의 lambdas 리스트안에 두개의 람다표현식을 작성해야하며 주석으로 표시된 프린트가 출력결과로 나와야 합니다.

lambdas = [
    lambda x: 'SHORT_PASSWORD' if len(x) < 8 else None,
    lambda x: 'NO_CAPITAL_LETTER_PASSWORD' if not any((i.isupper()) for i in x) else None
]

def check_password_using_lambda(password):
    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print(check_password_using_lambda('123'))  # SHORT_PASSWORD
print(check_password_using_lambda('12356789f'))  # NO_CAPITAL_LETTER_PASSWORD
print(check_password_using_lambda('123456789fF'))  # True
