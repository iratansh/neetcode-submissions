class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word

    def search(self, word: str) -> bool:
        # run a dfs to find the word in trie
        curr = self.root

        def dfs(i, node):
            if i == len(word):
                return node.word is not None
            
            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if ch not in node.children: return False
                return dfs(i + 1, node.children[ch])

        return dfs(0, curr)



