# 50명이 승객별 운행소요시간5~50분. 그중 5~15분인 승객만매칭.
from random import randint

def random_list(size):
    random_list = []
    i = 1
    for i in range(size):
        random_list.append(randint(5, 50))
    return random_list

n = 0
for i, time in enumerate(random_list(50)):
    if 5 <= time <= 15:
        print(f'[o] {i+1}번째 손님 (소요시간 : {time}분)')
        n += 1
    else:
        print(f'[x] {i+1}번째 손님 (소요시간 : {time}분)')
print('총탑승승객',n)
