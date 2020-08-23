# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
# def display():
#     print('display 함수가 실행됐습니다')
#
# decorated_display = decorator_function(display)
#
# decorated_display()


# def decorator_multi(func):
#     def wrapper(*args, **kwargs):
#         print(0)
#         return func(*args, **kwargs)
#     return wrapper
#
# @decorator_multi
# def mul(a, b,c):
#     print(a*b,c)
#
# mul(3, 4,6)

# 얘가 데코레이터
def decorator(func):
    def decorator(*args, **kwargs):
        print("%s %s" % (func.__name__, "before"))
        result = func(*args, **kwargs)
        print("%s %s" % (func.__name__ , "after"))
        return result
    return decorator

# 함수에 데코레이터를 붙여준다.
@decorator
def func(x, y):
    print(x + y)
    return x + y

func(1,2)