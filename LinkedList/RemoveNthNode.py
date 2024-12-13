# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = current = head
        count = 1
        ans = previous
        while count < (n + 1):
            count += 1
            current = current.next
        if current is None:
            head = head.next
            return head
        while current.next:
            previous = previous.next
            current = current.next

        if previous.next is None:
            return
        else:
            previous.next = previous.next.next
        return ans   