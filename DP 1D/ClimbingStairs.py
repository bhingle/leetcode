class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1 = 1
        n2 = 2
        if n == 1:
            return n1
        elif n == 2:
            return n2
        solution = 0
        for i in range(n - 2):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return temp


        