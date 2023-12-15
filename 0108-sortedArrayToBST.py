"""Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree."""

import printTree from 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # height balanced BST
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:    

        if len(nums) == 0: 
            return None
        
        rootNode = len(nums)//2
        root = TreeNode(nums[rootNode])
        root.left = self.sortedArrayToBST(nums[:rootNode]) # until root node
        root.right = self.sortedArrayToBST(nums[rootNode+1:]) # after root node

        return root

sol = Solution().sortedArrayToBST(nums = [-10,-3,0,5,9])

printTree(sol)