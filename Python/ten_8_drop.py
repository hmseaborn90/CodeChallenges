def fibonacciSimpleSum2(num):
    seq = fibonSeq(num)
    for i in seq:


        if i > num // 2:
            print(i, num)
            return False
        elif num - i in seq:
            return True
    
def fibonSeq(max_num):
    seq = [0,1]
    
    while seq[-1] < max_num:
        print(f"{seq[-1]} < {max_num}")
        seq.append(seq[-2] + seq[-1])
    return seq    

    # fibon = [0,1]
    # count = 2
    
    # while fibon[count-1] + fibon[count-2] < n:
    #     print('c',fibon[count -2])
    #     fibon.append(fibon[count -1] + fibon[count - 2])
    #     count += 1
    # print('f',fibon)   
    # for i in range(count):
    #     print('t',fibon[i] + fibon[count -1])
    #     if fibon[i] + fibon[count -1] == n:
    #         return True
            
    # return False


def csSearchRotatedSortedArray(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1


# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
#     def insert(self, value):
#         if value >= self.value:
#             if self.right is None:
#                 self.right = BinarySearchTree(value)
#             else:
#                 self.right.insert(value)
#         else:
#             if self.left is None:
#                 self.left = BinarySearchTree(value)
#             else:
#                 self.left.insert(value)

#     def contains(self, target):
#         if target == self.value:
#             return True
#         if target < self.value:
#             if not self.left:
#                 return False
#             else:
#                 return self.left.contains(target)
#         else: 
#             if not self.right:
#                 return False 
#             else:
#                 return self.right.contains(target)
def csBinarySearch(nums, target):
    lowest_index = 0
    highest_index = len(nums) - 1
    
    while highest_index >= lowest_index:
        search_i = (lowest_index + highest_index) // 2
        check_val = nums[search_i]
        
        if check_val == target:
            return search_i
        if check_val > target:
            highest_index = search_i - 1
        else:
            lowest_index = search_i + 1
    return -1
    

# def csBinarySearch(nums, target):
#     b_tree = BinarySearchTree(nums[0])
#     for i in range(len(nums)):
#         b_tree.insert(nums[i])
#     if b_tree.contains(target):
#         return target


# def csBinarySearch(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
    
#     return -1
def validBracketSequence(sequence):
    opens = tuple("({[")
    closings = tuple(")}]")
    temp_dic = dict(zip(opens, closings))
    print(opens)
    print(closings)
    print(temp_dic)
    stack = []
    
    for i in sequence:
        if i in opens:
            stack.append(temp_dic[i])
            print("tem", temp_dic[i])
        elif i in closings:
            print('idk',stack)
            if not stack or i != stack.pop():
                return False
    if not stack: 
        return True
    return False


    class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        while not left.isEmpty():
            right.push(left.pop())
        left.push(x)
        while not right.isEmpty():
            left.push(right.pop())
                    
    def remove():
        return left.pop()
        
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(head, value):
    new_node = ListNode(value)
    if head is None:
        return new_node
    if value < head.value:
        new_node.next = head
        return new_node
    curr_node = head
    
    while curr_node.next is not None:
       if curr_node.next.value > value:
            break
       else:
            curr_node = curr_node.next
        
    new_node.next = curr_node.next
    curr_node.next = new_node
    return head

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

            

class ListNode(object):
    _slots_ = ('value', 'next')

    def __init__(self, x):
        self.value = x
        self.next = None


class Tree(object):
    _slots_ = ('value', 'left', 'right')

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


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

