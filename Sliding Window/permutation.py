class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashMap1 = {}
        for i in s1:
            hashMap1[i] = hashMap1.get(i,0) + 1
        l,r  = 0, 0
        hashMap2 = {}
        while r < len(s1)-1:
            hashMap2[s2[r]] = hashMap2.get(s2[r],0) + 1
            r += 1
        while r < len(s2):
            hashMap2[s2[r]] = hashMap2.get(s2[r],0) + 1
            if hashMap1 == hashMap2:
                return True
            hashMap2[s2[l]] = hashMap2.get(s2[l],0) - 1
            if hashMap2.get(s2[l],0) == 0:
                del hashMap2[s2[l]]
            l += 1
            r += 1
        return False