class Node:
    """더블리 링크드 노드(이중연결리스트)"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """더블리 링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제연산"""

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node_to_delete:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드."""

        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고 있는 노드 리턴.없으면 None 리턴."""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드."""
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += "{}|".format(iterator.data)
            iterator = iterator.next

        return res_str

my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)