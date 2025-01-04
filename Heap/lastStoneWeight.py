class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a == b:
                pass
            else:
                heapq.heappush(stones,-abs(a-b))
        if len(stones):
            return -stones[0]
        return 0

