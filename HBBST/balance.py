class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
class SortedArrayToBST:
    def sortedArray(self, nums):
        return self.sortedArray(nums, 0, len(nums) - 1)
    
    def Sortedarray(self, nums, left, rigt):
        if left > right:
            return None
    
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
    
        root.left = self.Sortedarray(nums, left, mid -1)
        root.right = self.Sortedarray(nums, mid + 1, right)
    
    
        return root            
        
        
 #Example usage
        