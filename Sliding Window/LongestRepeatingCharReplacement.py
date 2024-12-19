class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        ans = 0
        while r < len(s):
            windowSize = r-l+1
            count[s[r]] = count.get(s[r],0) + 1
            #check if window is invalid
            #keep on shifting the l pointer until we find a valid window
            while windowSize - max(count.values()) > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
                windowSize = r-l + 1

            ans = max(ans,windowSize)
            r += 1
        return ans