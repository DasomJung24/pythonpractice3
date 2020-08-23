#
# def annoy_o_tron(message):
#     def greeting(name):
#         print(f'{message} - {name}!')
#     return greeting
#
# hello_o_tron = annoy_o_tron('Hello')
#
# hello_o_tron('jane')

#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Result: {result}')
#         return result
#
#     return wrapper
#
#
# @logger
# def add(a, b):
#     return a + b
#
# result = add(20, 22)
# # print(result)

# def decorator(func):
#     print('in decorator function')
#
#     def wrapper(*args, **kwargs):
#         print('in wrapper function')
#         func(*args, **kwargs)
#
#         return wrapper
#
# @decorator
# def greeting():
#     print('in greeting')

# def name_decorator(name):
# #     print(f'Hello, {name}')
# #    def decorated(*args):
#         print('start')
#         print(f'Hello, {name}')
#         print('end')
# #    return decorated
#
# @name_decorator('jane')
# def greeting():
#     print("Hello, ")\




# def name_decorator2(func):
#     def decorated():
#         print("hi")
#         func()
#         print("Hello, ")
#     return decorated()


# name_decorator = name_decorator2(func)
# name_decorator()



def name_decorator(name):
    def real_decorator(func):
        def wrapper():
            result = func()
            print(result,name)
            return result,name
        return wrapper()
    return real_decorator


@name_decorator("정우성")
def greeting():
    return "Hello, "





























