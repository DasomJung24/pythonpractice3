"""
힙
속성 - 완전 이진 트리이다.
파이선에서는 리스트를 이용하여 구현.

"""

# 최대힙의 정렬. / 부분적인 정렬만 가능하기 때문에 따로 공부 더 필요.
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    max_index = index

    if 0 < left_child_index < tree_size and tree[max_index] < tree[left_child_index]:
        max_index = left_child_index

    if 0 < right_child_index < tree_size and tree[max_index] < tree[right_child_index]:
        max_index = right_child_index

    if max_index != index:
        swap(tree, index, max_index)
        heapify(tree, max_index, tree_size)


# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)