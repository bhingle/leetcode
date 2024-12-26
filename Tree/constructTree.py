# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return 
        #first element of the preorder is the root
        tree = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        #Note - Each value of inorder also appears in preorder.
        #use the example to debug
        tree.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        tree.right = self.buildTree(preorder[mid+1:],inorder[mid + 1:])

        return tree