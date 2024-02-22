class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def deleteNode(root, key):
    if not root:
        return root


    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left


        temp_val = minValue(root.right)
        root.val = temp_val
        root.right = deleteNode(root.right, temp_val)
    return root


def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val


# Helper function to perform an in-order traversal of the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Creating a sample binary search tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Original Binary Search Tree:")
inorder_traversal(root)  # Output: 20 30 40 50 60 70 80
print("\n")

# Deleting a node with key 30
root = deleteNode(root, 30)
print("Binary Search Tree after deleting node with key 30:")
inorder_traversal(root)  # Output: 20 40 50 60 70 80

