class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if not (len(sentence1) == len(sentence2)):
            return False
        
        if sentence1 == sentence2:
            return True

        for i in range(len(sentence1)):
            if sentence1[i] not in similarPairs[i] or sentence2[i] not in similarPairs[i]:
                return False

        return True