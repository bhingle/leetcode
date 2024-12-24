# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isSame = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                self.isSame =  False
            self.isSameTree(p.left,q.left)
            self.isSameTree(p.right,q.right)
        elif p and not q:
            self.isSame =  False
        elif q and not p:
            self.isSame =  False
        return self.isSame