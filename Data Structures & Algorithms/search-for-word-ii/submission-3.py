class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
    
        return curr.word

    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        root = Trie()
        memory = set()
        for word in words:
            root.insert(word)
            
        def dfs(i, j, curr):
            if (i, j) in memory or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in curr.children:
                return
            
            memory.add((i, j))

        return ans