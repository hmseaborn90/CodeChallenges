# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def insertValueIntoSortedLinkedList(self, value):
    l_list= [value]
    while self is not None:
        l_list += self.value,
        self = self.next
    return sorted(l_list)







    # curr_node = head
    # while curr_node is not None:
    #     if curr_node.value + 1 == value:
    #         curr_node.next = ListNode(value)
    #         return head
    #     curr_node = curr_node.next

