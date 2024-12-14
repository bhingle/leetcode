"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        #hashMap
        #There will be a next and random value point to null. Hence adding None in hashMap
        copyOfNode = {None:None}
        while curr:
            copy = Node(curr.val)
            copyOfNode[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyOfNode.get(curr)
            copy.next = copyOfNode[curr.next]
            copy.random = copyOfNode[curr.random]
            curr = curr.next

        return copyOfNode[head]  