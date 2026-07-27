# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            
            lb, lh = dfs(node.left)
            rb, rh = dfs(node.right)
            balanced = lb and rb and abs(lh - rh) <= 1
            return (balanced, 1 + max(lh, rh))
        
        return dfs(root)[0]