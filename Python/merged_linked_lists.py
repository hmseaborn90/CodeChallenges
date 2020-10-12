# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def mergeTwoLinkedLists(list_1, list_2):
    # if list_1 ==  None:
    #     return list_2
    # if list_2 == None:
    #     return list_1
    # if list_1.value < list_2.value:
    #     list_1.next = mergeTwoLinkedLists(list_1.next, list_2)
    #     return list_1
    # else:
    #     list_2.next = mergeTwoLinkedLists(list_1, list_2.next)
    #     return list_2
    l_list = []
    while list_1 is not None and list_2 is not None:
        if list_2.value < list_1.value:
            l_list.append(list_2.value)
            list_2 = list_2.next
        else:
            l_list.append(list_1.value)
            list_1 = list_1.next
    
    while list_1 is not None:
        l_list.append(list_1.value)
        list_1 = list_1.next
    while list_2 is not None:
        l_list.append(list_2.value)
        list_2 = list_2.next
    print(l_list.next())
    return l_list

            
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def mergeTwoLinkedLists(l1, l2):
    if l1 == None or l2 == None:
        return l1 or l2
    smart = curr = ListNode(None)
    
    while True:
        if l1.value < l2.value:
            curr.next = l1
            curr = curr.next
            if l1.next == None:
                curr.next = l2
                break
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            if l2.next == None:
                curr.next = l1
                break
            l2 = l2.next   
    return smart.next
    # if list_1 ==  None:
    #     return list_2
    # if list_2 == None:
    #     return list_1
    # if list_1.value < list_2.value:
    #     list_1.next = mergeTwoLinkedLists(list_1.next, list_2)
    #     return list_1
    # else:
    #     list_2.next = mergeTwoLinkedLists(list_1, list_2.next)
    #     return list_2
    # l_list = []
    # while list_1 is not None and list_2 is not None:
    #     if list_2.value < list_1.value:
    #         l_list.append(list_2.value)
    #         list_2 = list_2.next
    #     else:
    #         l_list.append(list_1.value)
    #         list_1 = list_1.next
    
    # while list_1 is not None:
    #     l_list.append(list_1.value)
    #     list_1 = list_1.next
    # while list_2 is not None:
    #     l_list.append(list_2.value)
    #     list_2 = list_2.next
    
    # return l_list

            
