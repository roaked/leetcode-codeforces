"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepthBF(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + rightDepth
        
        if not root.right:
            return 1 + leftDepth        
        
        return min(leftDepth, rightDepth) + 1
    
    def minDepth(self, root: TreeNode) -> int:
        
        self.min_Depth = float('inf')
        self.dfs(root, 0)
        return self.min_Depth
    
    def dfs(self, node, cur_depth):
        if not node: #exit dfs recursion
            return
        
        if not node.left and not node.right:
            self.min_Depth = min(self.min_Depth, cur_depth + 1)
        
        self.dfs(node.left, cur_depth +1)
        self.dfs(node.right, cur_depth +1)

    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
res = (sol.minDepth(root))
print(res)