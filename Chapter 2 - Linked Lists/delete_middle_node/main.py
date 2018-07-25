class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node_from_list(node):
    # Given a node in the middle of a list, remove it from the list

    # a -> b -> c -> d, if given c, the new list should be a -> b -> d


    # We are not actually getting rid of pointer to current_node, but simulating deletion by
    # changing this nodes value to value of next node, and then skipping over the next node
    node.value = node.next.value
    node.next = node.next.next

def print_list(head):

    current_node = head

    while current_node != None:
        print(current_node.value)
        current_node = current_node.next


head = Node(100)
head.next = Node(200)
head.next.next = Node(300)

print(print_list(head))

delete_node_from_list(head.next)

print(print_list(head))