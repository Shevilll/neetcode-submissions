class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def s(curr, i):
            for c in range(i, len(word)):
                if word[c] == '.':
                    for ec in list(curr.children.keys()):
                        if not s(curr.children[ec], c + 1):
                            return False
                        else:
                            return True
                if word[c] not in curr.children:
                    return False
                curr = curr.children[word[c]]
            return curr.word
        
        return s(self.root, 0)

