class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Find the instersection of slow and fast pointer
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #create a slow2 pointer and find its intersection with slow
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow