# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self,p,q):
        if not p and not q:
            return True
        if p and q:
            if p.val == q.val:
                return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot and not root:
            return False
        #A null subRoot can be a sub tree of root
        if not subRoot and root:
            return True

        if self.isSame(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
