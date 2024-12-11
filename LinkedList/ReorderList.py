# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #splitting the list
        #slow and faster pointer helps to divide list into halves.
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing the second half of the list
        second = slow.next #second list begins after the first pointer
        slow.next = None # point last node of the first list to None
        previous = None
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        
        #merging the list
        second = previous
        first = head
        mod = 1
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

                
        