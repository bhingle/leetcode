# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isBal = True
    def calHeight(self, root):
        if root is None:
            return 0
        
        leftHeight = self.calHeight(root.left)
        rightHeight = self.calHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            self.isBal = False
        return 1 + max(leftHeight,rightHeight)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.calHeight(root)
        return self.isBal