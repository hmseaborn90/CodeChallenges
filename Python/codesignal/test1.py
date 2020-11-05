class Node:

    # Function to initialise the node object
    def __init__(self, value=None):
        self.value = value  # Assign value
        self.next = None  # Initialize next as null


class linked_list:

    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def add_head(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def add_tail(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    l_list = linked_list()
    l_list.print_list()
    l_list.head = Node(1)
    l_list.add_head(0)
    l_list.add_head(5)
    l_list.add_head(5)
    l_list.add_head(1)
    l_list.add_head(2)
    l_list.add_head(5)
    l_list.add_head(2)


    l_list.print_list()

def condense_linked_list(node):
    prev = None
    curr = node

    item_set = set()

    while curr:
        if curr.value in item_set:
            prev.next = curr.next
        else:
            item_set.add(curr.value)
            prev = curr
        curr = prev.next
    return node

condense_linked_list(l_list.head)