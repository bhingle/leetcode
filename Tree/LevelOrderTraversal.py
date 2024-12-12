from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)