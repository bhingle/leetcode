class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            #swap the left and right child recursively 
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root