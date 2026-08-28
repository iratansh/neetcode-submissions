class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # just iterate through the zip of each word in words? and compare the chars with the ordering of order?
        order_map = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False
                    break
            else:
                # no mismatch found so w1 cant be longer than w2
                if len(w1) > len(w2):
                    return False
        return True