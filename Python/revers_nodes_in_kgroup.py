# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(head, count):
    if count == 1 or head.next is None:
        return head
    
    return_value, current, prev_tail = reverse_list(head, count)
    while check_len(current, count):
        prev_prev_tail = prev_tail
        new_head, current, prev_tail = reverse_list(current, count)
        prev_prev_tail.next = new_head
        # current.next, current = reverse_list(current, count)
    return return_value
def reverse_list(head, count):
    current = head
    last_node, next_node = None, None
    length = 0
    while length < count:
        next_node = current.next
        current.next = last_node
        last_node = current
        current = next_node
        length += 1
    head.next = next_node
    
    return last_node, next_node, head
    
    
def check_len(head, count):
    if head is None:
        return False
        
    length = 1
    current = head
    
    while current.next is not None and length < count:
        length += 1
        current = current.next
    return length == count
