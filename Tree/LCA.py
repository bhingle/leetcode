# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            #p and q on one side
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # else:
            #     return curr
            #if you add the else block then the below code is not required because you are return curr anyways.

            #splitting
            if p.val < curr.val and q.val > curr.val:
                return curr
            if q.val < curr.val and p.val > curr.val:
                return curr
            
            #Either p/q is the root
            if p.val == curr.val:
                return curr
            elif q.val == curr.val:
                return curr