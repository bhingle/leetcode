import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        for i in tasks:
            hashMap[i] = hashMap.get(i,0) + 1
        heap = []
        for value in hashMap.values():
            heapq.heappush(heap, -value)
        queue = deque() # pairs of [-taskTime, idleTime]
        currentTime = 0
        while heap or queue:
            if heap:
                taskTime  = heapq.heappop(heap)
                #reducing the interval (+1 because of max heap)
                taskTime += 1
                currentTime += 1
                if taskTime == 0:
                    pass
                else:
                    queue.append([taskTime, currentTime + n])
            else:
                #ideal time
                currentTime += 1
            if queue and queue[0][1] == currentTime:
                heapq.heappush(heap,queue[0][0])
                queue.popleft()
        return currentTime

