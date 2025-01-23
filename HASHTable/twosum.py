class Solution:
    def twoSum(self, nums, target):
        soln = {}
        for i, s in range(nums):
            rem = target - s
            if rem in soln:
                return [seen[rem], i]
            soln[s] = i
        return []    
    
    
        