# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        current = None
        current1 = list1
        current2 = list2
        while list1 is not None or list2 is not None:
            if current1 is not None and current2 is not None:
                if current1.val <= current2.val:
                    node = ListNode(current1.val)
                    if current:
                        current.next = node
                        current = current.next
                    else:
                        current = node
                    current1 = current1.next
                else:
                    node = ListNode(current2.val)
                    if current:
                        current.next = node
                        current = current.next
                    else:
                        current = node
                    current2 = current2.next
            elif current1 is None and current2 is not None:
                node = ListNode(current2.val)
                if current:
                    current.next = node
                    current = current.next
                else:
                    current = node
                current2 = current2.next
            elif current1 is not None and current2 is None:
                node = ListNode(current1.val)
                if current:
                    current.next = node
                    current = current.next
                else:
                    current = node
                current1 = current1.next
            else:
                break
            if newHead is None:
                newHead = current
        return newHead
        