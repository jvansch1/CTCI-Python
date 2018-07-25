class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, head = Node(100)):
        self.head = head

    def get_head(self):
        return self.head

    def add_node(self, node):
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node

    def print_list(self):
        current_node = self.head

        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next

        print(current_node.value)


def remove_dups_from_linked_list(head):
    seen_values = {}
    current_node = head
    previous_node = None

    while current_node.next != None:
        if current_node.value in seen_values:
            node_after_next = current_node.next
            previous_node.next = node_after_next
        else:
            seen_values[current_node.value] = True

        previous_node = current_node
        current_node = current_node.next

list = LinkedList()
list.add_node(Node(5))
list.add_node(Node(567))
list.add_node(Node(3000))
list.add_node(Node(567))
list.add_node(Node(283478))
deleted_list = remove_dups_from_linked_list(list.get_head())
list.print_list()