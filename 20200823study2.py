# 1.다음과 같은 도시목록의 리스트가 주어졌을때, 도시이름이 S로 시작하지 않는 도시만 리스트로 만들 때 리스트 컴프리헨션을 사용하여 함수를 작성해 보세요.

# cities = ["Tokyo","Shanghai","Jakarta","Seoul","Guangzhou","Beijing","Karachi","Shenzhen","Delhi"]
#
# cities_not_start_s = [i for i in cities if i[0] != 'S']
#
# print(cities_not_start_s)


# 2.다음과 같은 도시, 인구수가 튜플의 리스트로 주어졌을때, 키가 도시, 값이 인구수인 딕셔너리를 딕셔너리 컴프리헨션을 사용한 함수를 작성해 보세요.

# population_of_city = [('Tokyo',36923000), ('Shanghai',34000000), ('Jakarta', 30000000), ('Seoul', 25514000),
#  ('Guangzhou', 25000000), ('Beijing', 24900000), ('Karachi', 24300000), ('Shenzhen', 23300000), ('Delhi', 21753486)]
#
# dict_city = {i:j for i, j in population_of_city}
#
# print(dict_city)
# print(type(dict_city))
#
# a = [1, 2, 3]
#
# I = iter(a)
#
# while True:
#     try:
#         X = next(I)
#     except StopIteration:
#         break
#     print(X**2, end=' ')

# 다음의 간단한 키를 출력하는 딕셔너리에 대한 for 문을 while문으로 구현해 보세요.
#
# D = {'a':1, 'b':2, 'c':3}
# for key in D.keys():
#     print(key)
#
# D_2 = iter(D)
# while True:
#     try:
#         key = next(D_2)
#     except StopIteration:
#         break
#     print(key)
#
# def test_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = test_generator()
# print(type(gen))
#
# for i in test_generator():
#     print(i)

# def three_generator():
#     a = [1, 2, 3]
#     yield from a
#
# g = three_generator()
# print(list(g))

# 클래스로 iterator 구현.
# class MyCollection:
#     def __init__(self):
#         self.size = 10
#         self.data = list(range(self.size))
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index >= self.size:
#             raise StopIteration
#
#         n = self.data[self.index]
#         self.index += 1
#         return n
#
# coll = MyCollection()
# for x in coll:
#     print(x)
# #
# #  Generator Expression
# g = (i*i for i in range(20))
#
# for i in range(10):
#     value = next(g)
#     print(value)
#
# print('10 finish')
#
# for i in g:
#     print(i)
#
# # send 함수.
#
# def generator_send():
#     received_value = 0
#
#     while True:
#         received_value = yield
#         print("received_value = ", end='')
#         print(received_value)
#         yield received_value * 2
#
# gen = generator_send()
# next(gen)
# print(gen.send(2))
#
# next(gen)
# print(gen.send(3))
#
# a = [1, 2, 3]
#
# def generate_square_list():
#     result = (x*x for x in a)
#     yield from result
#
# g = generate_square_list()
# print(list(g))
#

# def print_iter(iter):
#     for element in iter:
#         print(element)
#
# print_iter(generate_square_list())
#
# # 피보나치 제너레이터구현.

# def fibonacci_func(n):
#     a, b = 0, 1
#     i = 0
#     while True:
#         if i > n:
#             return
#         yield a
#         a, b = b, a+b
#         i += 1
#
# fib = fibonacci_func(10)
#
# def three_generator():
#     a = [1, 2, 3]
#
#     yield a
#
# gen = three_generator()
#
# print(list(gen))

# import time
#
#
# L = [1, 2, 3]
#
# def print_iter(iter):
#     for element in iter:
#         print(element)
#
# def lazy_return(num):
#     print("sleep 1s")
#     time.sleep(1)
#     return num

# print("comprehension_list=")
# comprehension_list = [lazy_return(i) for i in L]  # sleep1s 는 1초 간격으로 출력. 1 2 3 은 한번에 쭈루룩 출력.
# # # print(comprehension_list)
# # """
# 출력값.
# comprehension_list=
# sleep 1s
# sleep 1s
# sleep 1s
# [1, 2, 3]
# """
# print_iter(comprehension_list)
#
# print("generator_exp=")
# generator_exp = (lazy_return(i) for i in L)   # sleep 1s 출력, 1과 sleep 1s 출력 , 2와 sleep 1s 출력..
# # # print(generator_exp)
# # """
# # 출력값.
# # generator_exp=
# # <generator object <genexpr> at 0x102a8c190>
# # """
# print_iter(generator_exp)
#
# a = lambda x, y, z: x + y + z
# print(a)
# print(a(1, 2, 3))

# def square(x):
#     return x ** 2
#
# def power_3(x):
#     return x ** 3
#
# def power_4(x):
#     return x ** 4
#
# powers = [square, power_3, power_4]
#
# for f in powers:
#     print(f(2))

# Lambdas = [
#     lambda x: x ** 2,
#     lambda x: x ** 3,
#     lambda x: x ** 4
# ]
#
# for lambda_fuc in Lambdas:
#     print(lambda_fuc(2))
#
# import types
#
# f = lambda x, y, z: x + y + z
#
# print(f)
# print(type(f))
# print(type(f) == types.LambdaType)
#
# print(dir(types))

