class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        part = []
        def isPalindrome(i,j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                    pass
                else:
                    return False
            return True
        def backtracking(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    part.append(s[i:j+1])
                    backtracking(j+1)
                    part.pop()
           
        backtracking(0)
        return res
    