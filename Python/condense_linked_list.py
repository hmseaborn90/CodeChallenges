# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

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