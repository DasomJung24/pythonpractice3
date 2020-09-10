# 함수의 시작과 끝을 출력하는 데코레이터

# def trace(func):
#     def wrapper():
#         print(func.__name__, '함수 시작')
#         func()
#         print(func.__name__, '함수 끝')
#     return wrapper
#
# @trace
# def hello():
#     print('hello')
#
# @trace
# def world():
#     print('world')

# 매개변수와 반환값을 처리하는 데코레이터 만들기
#
# def trace(func):
#     def wrapper(a, b):
#         r = func(a, b)
#         print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
#         return r
#     return wrapper
#
# @trace
# def add(a, b):
#     return a + b
#
# print(add(10, 20))

# 가변 인수 함수 데코레이터 만들기

# def trace(func):
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs)
#         print('{0}(args={1}, kwargs={2} -> {3}'.format(func.__name__, args, kwargs, r))
#
#         return r
#     return wrapper
#
# @trace
# def get_max(*args):
#     return max(args)
# @trace
# def get_min(**kwargs):
#     return min(kwargs.values())
#
# print(get_max(10, 20))
# print(get_min(a=10, b=20, c=30))

# 매개변수가 있는 데코레이터 만들기
#
# def is_multiple(x):
#     def real_decorator(func):
#         def wrapper(a, b):
#             r = func(a, b)
#             if r % x == 0:
#                 print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
#             else:
#                 print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
#             return r
#         return wrapper
#     return real_decorator
#
# @is_multiple(3)
# def add(a, b):
#     return a + b
#
# print(add(10, 10))
# print(add(3, 6))

# 클래스로 데코레이터 만들기

# class Trace:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print(self.func.__name__, '함수 시작')
#         self.func()
#         print(self.func.__name__, '함수 끝')
#
# @Trace
# def hello():
#     print('hello')
#
# hello()

# 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기

# class Trace:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         r = self.func(*args, **kwargs)
#         print('{0}(args={1}, kwargs={2} -> {3}'.format(self.func.__name__, args, kwargs, r))
#
#         return r
#
# @Trace
# def add(a, b):
#     return a + b
#
# print(add(29, 40))

# 클래스로 매개변수가 있는 데코레이터 만들기

class IsMultiple:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper

@IsMultiple(3)
def add(a, b):
    return a + b

print(add(19, 40))
print(add(4, 1))