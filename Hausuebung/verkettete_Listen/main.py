import random


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = self.head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

    def add_node_at_end(self, node):
        newNode = Node(node)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def length(self):
        index = 0
        current = self.head
        while current is not None:
            current = current.next
            index += 1
        print(index)

    def print_all_items(self):
        for item in self:
            print(item, end=" ")

if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(10):
        random_number = random.randint(1, 100)
        linked_list.add_node_at_end(random_number)

    linked_list.length()
    linked_list.print_all_items()
