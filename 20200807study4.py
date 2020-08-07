# 1000미만의 자연수에서 3과 5의 배수의 총합.

def multi_sum(a, b):
    result = 0
    for i in range(1, 1000):
        if i % a == 0 or i % b == 0:
            result += i
    return result

print(multi_sum(2, 5))
