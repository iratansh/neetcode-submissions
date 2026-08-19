from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)     # userId: [(time, tweetId)]
        self.following = defaultdict(set)   # userId: Set<Followee>  <-- renamed
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        user_list = self.following[userId] | {userId}

        for followee_id in user_list:
            if self.tweets[followee_id]:
                idx = len(self.tweets[followee_id]) - 1
                t, tweet_id = self.tweets[followee_id][idx]
                heapq.heappush(heap, (-t, tweet_id, followee_id, idx - 1))

        while heap and len(res) < 10:
            _, tweet_id, followee_id, next_idx = heapq.heappop(heap)
            res.append(tweet_id)

            if next_idx >= 0:
                prev_t, prev_tweet_id = self.tweets[followee_id][next_idx]
                heapq.heappush(heap, (-prev_t, prev_tweet_id, followee_id, next_idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)