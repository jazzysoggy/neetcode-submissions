class Twitter:

    def __init__(self):
        self.tweet_matrix = defaultdict(list)

        self.follower_matrix = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_matrix[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for tweet in self.tweet_matrix[userId]:
            heap.append(tweet)

        for user in self.follower_matrix[userId]:
            for tweet in self.tweet_matrix[user]:
                heap.append(tweet)

        heapq.heapify(heap)

        output = []

        i = 0
        while len(heap) > 0 and i < 10:
            time, curr = heapq.heappop(heap)
            output.append(curr)
            i += 1

        return output
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower_matrix[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_matrix[followerId]:
            self.follower_matrix[followerId].remove(followeeId)
        
