#Similar leaf

#Consider all the leaves of a binary tree, 
# from left to right order, the values of those leaves form a leaf value sequence.
#Two binary trees are considered leaf-similar if their leaf value sequence is the same. 
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def simpleLeaf(root1, root2):
    def Tree(node, leaves):
        if not node:
            return
        if not node.left and notnode.right:
            leaves.append(node.val)
                
        Tree(node.left, leaves)
        Tree(node.right, leaves)    
            
        leaves1, leaves2 = [], []
            
        Tree(root1, leaves1)
        Tree(root2, leaves2)
            
        return leaves1 == leaves2
    
   