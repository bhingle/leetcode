class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        #Keep A as smaller
        if len(B) < len(A):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A) - 1
        #binary search on smaller array i.e. A
        while True:
            i = (l + r) // 2 #A - middle index of A
            j = half - i - 2 #B - middle index of B (-2 because indexing start from 0)


            #To ensure index doesn't go out of range, adding -inf and inf
            Aleft = A[i] if i >=0 else -float('inf')
            Aright = A[i + 1] if i <len(A) - 1 else float('inf')
            Bleft = B[j] if j >=0 else -float('inf')
            Bright = B[j + 1] if j <len(B) - 1 else float('inf')

            #partition is correct
            if Bleft <= Aright and Aleft <= Bright:
                #odd
                if total % 2:
                    return min(Aright,Bright)
                #even
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1            