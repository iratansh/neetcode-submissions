class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # return all possible sentences
        root = TrieNode()

        # append all words to the trie
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
        
        res = []
        # want to be performing backtracking utilizing the trie
        def backtrack(i, path): # need to keep track of which char we are on in s
            if i == len(s):
                res.append(" ".join(path))
                return
            

            curr = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in curr.children:
                    return
                
                curr = curr.children[ch]
                if curr.word is not None:
                    path.append(curr.word)

                    backtrack(j + 1, path)

                    path.pop()
                
        backtrack(0, [])
        return res