class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # put dictionary into a trie? and then iterate through s and try to match words in s to words in
        # The trie?
    
        root = TrieNode()
        
        for word in dictionary:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
        
        # dfs(i) returns the min extra chars needed for the subtstring starting at s[i:]
        memo = {len(s): 0}


        def dfs(i):
            if i in memo:
                return memo[i]
            
            # option 1: skip s[i]?
            res = 1 + dfs(i + 1)

            # option 2: take s[i]?
            nonlocal root
            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word is not None:
                    res = min(res, dfs(j + 1)) 
            memo[i] = res
            return res
        return dfs(0)