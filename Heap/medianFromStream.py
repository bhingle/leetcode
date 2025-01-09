import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        #Adding first element to heap
        if not self.maxHeap and  not self.minHeap:
            heapq.heappush(self.minHeap,num)
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap,num)
            else:
                heapq.heappush(self.maxHeap,-num)
            #Balance the heap
            if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
                if len(self.minHeap) > len(self.maxHeap):
                    heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                else:
                    heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            


    def findMedian(self) -> float:
        #even length
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0 :
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        else:
            #odd length
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()