class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
def maxDepth(root):
    if not root:
        return 0
        
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)
    
    
root = TreeNode(3)    
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Maximum Depth:", maxDepth(root))    