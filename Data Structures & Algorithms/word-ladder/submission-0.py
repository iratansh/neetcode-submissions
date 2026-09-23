class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # transform beginword to endword 
        # can transform beginWord to any word within wordList
        if beginWord == endWord: return 0
        if endWord not in wordList: return 0

        # basically iterate through all words in wordsList and construct a adj list 
        n, m = len(wordList), len(wordList[0])
        adj = defaultdict(list)

        for word in wordList:
            for i in range(m):
                s = word[:i] + "*" + word[i + 1:]
                adj[s].append(word)
        
        q = deque([(beginWord, 0)])
        visited = set()
        visited.add(beginWord)

        while q:
            node, seq = q.popleft()

            if node == endWord:
                return seq + 1
            
            for i in range(m):
                s = node[:i] + "*" + node[i + 1:]
                for nei in adj[s]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, seq + 1))
        return 0

        
                