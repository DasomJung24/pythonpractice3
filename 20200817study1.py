"""
순회
자료구조에 저장된 모든 데이터를 도는 것

트리순회 - 재귀함수 사용

순회의 기본 동작들
- 재귀적으로 왼쪽 부분 트리 순회
- 재귀적으로 오른쪽 부분 트리 순회
- 현재 노드 데이터 출력
전위 순회( pre-order 순회) D L R 
- 현재 노드 데이터 출력
- 재귀적으로 왼쪽
- 재귀적으로 오른쪽
후위 순회 (post-order 순회) L R D
- 재귀적으로 왼쪽
- 재귀적으로 오른쪽
- 현재 노드 데이터 출력
중위순회 (in-order 순회) L D R
- 재귀적으로 왼쪽
- 현재 노드 데이터 출력
- 재귀적으로 오른쪽
"""

# 중위순회 (in-order 순회)

class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

def traverse_inorder(node):
    """in-order 순회 함수"""
    if node is not None:
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)


# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order로 순회한다
traverse_inorder(root_node)