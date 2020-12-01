"""
x개의 닫힌 문이 있다.
n명의 사람이 문앞을 지나가며 자신의 순번의 배수에 해당하는 문을 열거나 닫는다. 열린문은 닫고 닫힌 문은 연다.
문의 개수를 x, 사람의 수를 n으로 입력받아 위의 행동을 마친 뒤 최종적으로 열려있는 문의 개수를 출력해라.
"""


def find_open_door(x, n):
    doors = ['close' for door in range(x)]
    for person in range(n):
        for door in range(len(doors)):
            if (door+1) % (person+1) == 0:
                if doors[door] == 'close':
                    doors[door] = 'open'
                else:
                    doors[door] = 'close'

    print(doors.count('open'))

find_open_door(20, 4)