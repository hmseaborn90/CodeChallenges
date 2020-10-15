#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
def balancedBinaryTree(root):
    if root is None:
        return True
        
    left_height = height(root.left)
    right_height = height(root.right)
    if(abs(left_height - right_height) <= 1) and balancedBinaryTree(root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    
    return False


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    if root is None:
        return 0
        
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return minimumDepthBinaryTree(root.right) +1
    
    if root.right is None:
        return minimumDepthBinaryTree(root.left) +1
        
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) +1
