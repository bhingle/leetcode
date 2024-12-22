# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    #Function to return the maximum height from left/right subtree
    def calMaxHeight(self,root):
        if root is None:
            return 0
   
        leftHeight = self.calMaxHeight(root.left)
        rightHeight = self.calMaxHeight(root.right)
        #update the class variable - maxheight
        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
        return 1 + max( leftHeight , rightHeight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:       
        self.calMaxHeight(root)
        return self.maxDiameter