# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = None
        while l1 and l2:
            ans = l1.val + l2.val + carry
            carry = ans // 10
            if curr is None:
                curr = ListNode(ans % 10) 
                head = curr
            else:
                curr.next = ListNode(ans % 10)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            ans = l1.val + carry
            carry = ans // 10
            curr.next = ListNode(ans % 10)
            curr = curr.next 
            l1 = l1.next

        while l2:
            ans = l2.val + carry
            carry = ans // 10
            curr.next = ListNode(ans % 10)
            curr = curr.next 
            l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return head