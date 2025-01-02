import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for point in points:
            distance = math.pow(point[0],2) + math.pow(point[1],2)
            heapq.heappush(ans,(-distance, point))
            if len(ans) > k:
                heapq.heappop(ans)
        solution = []
        for i in ans:
            solution.append(i[1])
        return solution
