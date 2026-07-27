# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self.result = 0

        # def dfs(node): 
        #     if not node:
        #         return 0
            
        #     left_height = dfs(node.left)
        #     right_height = dfs(node.right)

        #     self.result = max(self.result, left_height + right_height)
            
        #     return 1 + max(left_height, right_height)
        
        # dfs(root)
        # return self.result

        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height, left_dia = mp[node.left]
                right_height, right_dia = mp[node.right]

                mp[node] = (1 + max(left_height, right_height), 
                     max(left_height + right_height, left_dia, right_dia))
            
        return mp[root][1]