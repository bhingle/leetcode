class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l  = 0
        r = 1
        hashSet = set()
        hashSet.add(s[0])
        ans = 1
        while r < len(s):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                ans = max(len(hashSet),ans)
                r += 1
            else:
                #shift the left pointer until there are no duplicates
                while s[l] != s[r]:
                    hashSet.remove(s[l])
                    l += 1
                l += 1
                r += 1
        return ans

