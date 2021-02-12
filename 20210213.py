"""
프로그래머스 2단계 - 스킬트리
"""


def solution(skill, skill_trees):
    b = 0
    for node in skill_trees:
        temp_str = ''
        for i in range(len(node)):
            if node[i] in skill:
                temp_str += node[i]
        for j in range(len(temp_str)):
            if temp_str[j] != skill[j]:
                b += 1
                break
    return len(skill_trees) - b


skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']

print(solution(skill, skill_trees))
