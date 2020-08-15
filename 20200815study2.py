'''
해시테이블
해시 함수 - 특정 값을 원하는 범위의 자연수로 바꿔주는 함수
해시테이블은 해시함수와 배열을 같이 사용하는 구조
1고정된 크기의 배열을 만든다
2해시함수를 이용해서 key를 원하는 범위의 자연수로 바꾼다
3해시함수 결과값 인덱스에 key-value 쌍을 저장한다

충돌(collision)
이미 사용하고 있는 인덱스에 새로운 키밸류쌍을 또 저장해야 할 경우가 생기는데
이를 충돌이라고 한다
해시테이블에서는 충돌을 제대로 처리해줘야 한다
chaining
충돌이 일어나면 쇠사슬처럼 엮겠다는 뜻
충돌에 대비해서 각 인덱스에 링크드 리스트를 저장하는 것.
open addressing
충돌이 일어나면 다른 비어있는 인덱스를 찾아서 그곳에 데이터를 저장하는 방법.
비어있는 인덱스를 찾는 방법은 여러가지가 있지만 그중 가장 기본적인 방법인
선형탐사(linear probing) -> 충돌이 일어났을 때, 한칸씩 다음 인덱스가 비어있는지 확인.
* 제곱탐사(Quadratic probing) -> 충돌이 일어났을때, 1의제곱뒤의 인덱스확인, 꽉차있으면
2의 제곱뒤의 인덱스 확인, 3의제곱뒤의 인덱스 확인 ...


체이닝 시간복잡도 : 탐색, 저장, 삭제 -> O(n)  / 평균시간복잡도 -> O(1)
'''
# 체이닝을 링크드 리스트로 표현.

class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 키를 갖고 있는 노드를 리턴. 해당 노드가 없으면 None 리턴"""
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드. 맨 뒤 삽입."""
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        if self.head == self.tail:  # 마지막 데이터 삭제할때.
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:  # 제일 앞 데이터 삭제할때.
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:  # 제일 뒤 데이터 삭제할때.
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # 중간 데이터 삭제할때.
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        iterator = self.head

        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str


# 해시테이블 구현하기.

class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의 ; Key는 파이썬 불변 타입이어야 함.
        """
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        """주어진 key에 대응하는 인덱스에 저장된 링크드 리스트를 리턴하는 메소드"""
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def _look_up_node(self, key):
        """파라미터로 받은 Key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        """주어진 key에 해당하는 데이터를 리턴하는 메소드"""
        return self._look_up_node(key).value

    def insert(self, key, value):
        """
        새로운 key - 데이터 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 대응하는 데이터로 바꿔줌.
        """
        existing_node = self._look_up_node(key)

        if existing_node is not None:
            existing_node.value = value
        else:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        delete_key = self._look_up_node(key)

        if delete_key is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(delete_key)

    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]


test_scores = HashTable(50)

test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)