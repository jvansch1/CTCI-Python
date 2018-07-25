class Node():

    def __init__(self, value):
        self.value = value
        self.next = None



def sum_two_lists(list_one, list_two):
    new_list = None
    carry_over = None

    while list_one != None and list_two != None:
        new_amount = list_one.value + list_two.value

        if carry_over:
            new_amount += carry_over
            carry_over = None

        if new_amount > 10:
            carry_over = int(new_amount / 10)
            new_amount  = new_amount % 10

        if new_list == None:
            new_list = Node(new_amount)

        else:
            new_list.next = Node(new_amount)

        list_one = list_one.next
        list_two = list_two.next
        new_list = new_list.next

    return new_list





list_one = Node(7)
list_one.next = Node(1)
list_one.next.next = Node(6)

list_two = Node(5)
list_two.next = Node(9)
list_two.next.next = Node(2)

print(sum_two_lists(list_one, list_two))