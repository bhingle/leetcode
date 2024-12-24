# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        solution = []
        while queue:
            length = len(queue)
            rightSide = None
            for i in range(length):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                solution.append(rightSide.val)
        return solution
        