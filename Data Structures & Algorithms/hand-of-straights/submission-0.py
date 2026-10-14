class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # array hand such that we have groups of size groupsize and each card in the group is arranged in consecutive order increasing bby 1
        if len(hand) % groupSize != 0: return False

        # we dont really need to have the cards arranged or anything, all we are checkingn for is possibility
        # brute force: iterate across each group and try to fill it out one by one
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
            while heap and count[heap[0]] == 0:
                heapq.heappop(heap)
        return True