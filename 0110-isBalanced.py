"""Given a binary tree, determine if it is height-balanced."""

from operations import printTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.balanced = True

        def dfs(root):         
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if (abs(left - right) > 1):
                self.balanced= False

            return max(left, right) + 1
        
        dfs(root)       
        return self.balanced
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(Solution().isBalanced(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left= TreeNode(4)
root.left.left.right = TreeNode(4)

print(Solution().isBalanced(root))


root = []
sol = Solution()
res = (sol.isBalanced(root))

print(Solution().isBalanced(root))