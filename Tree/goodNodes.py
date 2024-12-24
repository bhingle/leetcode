# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        maximum = -float('inf')
        def dfs(root,maximum):
            if root == None:
                return 0
            if root.val >= maximum:
                ans = 1
            else:
                ans = 0    
            maximum = max(maximum, root.val)
            return ans + dfs(root.left,maximum) + dfs(root.right,maximum)
        return dfs(root, maximum)
        