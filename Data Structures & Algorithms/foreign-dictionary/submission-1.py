class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        # want to iterate through all words in words and build the dict?
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_l = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_l] == w2[:min_l]: return ""
            
            for j in range(min_l):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""



