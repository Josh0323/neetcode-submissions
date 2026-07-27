class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)
        min_heap = []
        for user in self.follow_map[userId]:
            if user in self.tweet_map:
                ind = len(self.tweet_map[user]) - 1
                c, i = self.tweet_map[user][ind]
                heapq.heappush(min_heap, (c, i, user, ind - 1))

        result = []
        while min_heap and len(result) < 10:
            _, i, u, ind = heapq.heappop(min_heap)
            result.append(i)
            if ind >= 0:
                c, i = self.tweet_map[u][ind]
                heapq.heappush(min_heap, (c, i, u, ind - 1))
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
