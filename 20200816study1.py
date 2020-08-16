"""
트리
데이터의 상-하관계(계층적관계)를 저장하는 자료구조
컴퓨터과학의 다양한 문제를 기발하게 해결할수 있음
흔히 사용하는 여러 추상 자료형 구현 가능
- 이진트리
각 노드가 최대 2개의 자식을 가질수 는 트리
-- 정 이진 트리 (full binary tree)
모든 노드가 2개 또는 0개의 자식노드를 갖는 트리
-- 완전이진트리(complete binary tree)
마지막 레벨 직전의 레벨까지는 모든 노드들이 다 채워지고 마지막 레벨에서는 왼쪽에서 오른쪽 순으로 노드들이 다 채워진 트리.
--포화이진트리(perfect binary tree)
모든 레벨이 노드로 빠짐없이 다 채워져있는 트
"""
# 이진트리 구현

class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

# 노드 인스턴스 생성
root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(7)
node_E = Node(11)

# B와 C를 root 노드의 자식으로 지정
root_node.left_child = node_B
root_node.right_child = node_C

# D와 E를 B의 자식으로 지정
node_B.left_child = node_D
node_B.right_child = node_E

# root 노드에서 왼쪽 자식 노드 받아오기
test_node_1 = root_node.left_child

print(test_node_1.data)

# 노드 B의 오른쪽 자식 노드 받아오기
test_node_2 = test_node_1.right_child

print(test_node_2.data)

# 파이썬 리스트로 완전이진트리 구현하기

def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    parent_index = index // 2
    if 0 < parent_index <= len(complete_binary_tree):
        return parent_index
    else:
        return None


def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    left_child_index = index * 2
    if left_child_index <= len(complete_binary_tree):
        return left_child_index

    return None


def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    right_child_index = index * 2 + 1
    if right_child_index <= len(complete_binary_tree):
        return right_child_index

    return None


# 실행 코드
root_node_index = 1  # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree, root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)