# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            if node is None:
                return head
            previous  = None
            current = node
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous
        def findKthNode(node,k):
            curr = node
            k-=1
            while curr is not None and k > 0:
                curr = curr.next
                k -= 1
            return curr
        temp = head
        prevNode = None
        while temp != None:
            kthNode = findKthNode(temp,k)
            if kthNode is None:
                if prevNode:
                    prevNode.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            #first group reversal
            reverse(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
          
        return head