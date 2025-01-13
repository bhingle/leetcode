class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        hashMap = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res = []
        part = []
        def backtracking(i):
            if i >= len(digits):
                res.append("".join(part[:]))
                return
            letters = list(hashMap.get(int(digits[i])))
            for letter in letters:
                part.append(letter)
                backtracking(i + 1)
                part.pop()
        backtracking(0)
        return res