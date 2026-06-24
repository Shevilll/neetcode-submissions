class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if not (len(sentence1) == len(sentence2)):
            return False
        
        hashset = set()

        for a, b in similarPairs:
            hashset.add((a, b))
            hashset.add((b, a))

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if (w1, w2) not in hashset:
                return False
            
        return True