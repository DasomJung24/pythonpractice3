# def func_param_with_var_args(name, age, *args):
#     print("name=",end=""), print(name)
#     print("args=",end=""), print(args)
#     print("age=",end=""), print(age)
#
# func_param_with_var_args("정우성", 20, "01012341234", "seoul")
#
# def func_param_with_kwargs(name, age, address=0, **kwargs):
#     print("name=",end=""), print(name)
#     print("age=",end=""), print(age)
#     print("kwargs=",end=""), print(kwargs)
#     print("address=",end=""), print(address)
#
#
# func_param_with_kwargs("정우성", "20", mobile="01012341234", address="seoul")

def mixed_params(age, name="아이유", *args, address, **kwargs):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)


mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")


#
# def func_param_with_var_args(name, *args, age):
#     print("name=",end=""), print(name)
#     print("args=",end=""), print(args)
#     print("age=",end=""), print(age)
#
#
# func_param_with_var_args("정우성", "01012341234", "seoul", age=20)

# def fn(name,  age=1, *args):
#     print(name, age)
#     print(args)
#
#
# fn('jane', 3, 4, 5, 6)