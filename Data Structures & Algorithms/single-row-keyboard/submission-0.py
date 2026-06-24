class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}

        for i in range(len(keyboard)):
            hashmap[keyboard[i]] = i

        ans = 0

        curr = 0

        for i in word:
            ans += abs(curr - hashmap[i])
            curr = hashmap[i]
        
        return ans