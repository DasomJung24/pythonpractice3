#
# class Database:
#
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#         self.name = {}
#
#     def insert(self, field, value):
#         if len(self.name) > self.size:
#             pass
#         else:
#             self.name[field] = value
#
#     def select(self, field):
#         if not field in self.name:
#             return None
#         else:
#             return self.name[field]
#
#     def update(self, field, value):
#         if not field in self.name:
#             pass
#         else:
#             self.name[field] = value
#
#     def delete(self, field):
#         if not field in self.name:
#             pass
#         else:
#             del self.name[field]
#
#
# C1 = Database('db', 3)
#
# C1.insert('a', 1)
# C1.insert('b', 2)
#
# print(C1)
#
"""
 Input으로 주어진 리스트에서 홀수는 전부 지우고 짝수만 남은 리스트를 리턴해주세요.
리스트의 요소들은 전부 숫자값이고 총 요소 수는 5개 입니다.

예를 들어, 다음과 같은 list가 input으로 주어졌다면:

[1, 2, 3, 4, 5]

다음과 같은 결과물이 리턴되어야 합니다.

[2, 4]
"""

import sys

print(sys.modules)

print(type(sys))








