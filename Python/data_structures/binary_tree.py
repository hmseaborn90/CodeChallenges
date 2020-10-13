class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print(f"traversal type {str(traversal_type)} is not supported")
    
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

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.balancedBinaryTree(1))