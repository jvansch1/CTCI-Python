class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



def kth_last(head, k):

    list_of_nodes = []

    current_node = head

    while current_node.next != None:
        list_of_nodes.append(current_node)
        current_node = current_node.next

    list_of_nodes.append(current_node)

    return list_of_nodes[-k]

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)

print(kth_last(head, 5).value)