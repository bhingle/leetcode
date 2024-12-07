# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # case 1 -> 0 child
        if root is None:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        #found the key
        else:
            # case 2 -> 1 child
            if root.right is None:
                return root.left
            #case 2 -> 1 child
            elif root.left is None:
                return root.right
						#case 3 - 2 childs ->  find the min of right subtree
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                #This will convert case 3 to either case 2/1
                root.right = self.deleteNode(root.right,curr.val)
        return root
        
        
            
        