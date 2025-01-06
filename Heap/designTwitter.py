import heapq
class Twitter:
    def __init__(self):
        self.followMap= defaultdict(set) # userId -> set of followeeId
        self.tweetMap = defaultdict(list) # userId -> list of [count,tweetId]
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for i in self.tweetMap[userId]:
            heapq.heappush(maxHeap,i)
        for i in self.followMap[userId]:
            for j in self.tweetMap[i]:
                heapq.heappush(maxHeap,j)
        ans = []
        print(maxHeap)
        while maxHeap:
            a = heapq.heappop(maxHeap)
            ans.append(a[1])
            if len(ans) == 10:
                break
        return ans

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)