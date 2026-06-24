class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashset = set()

        for i in s:
            if i in hashset:
                hashset.remove(i)
            else:
                hashset.add(i)

        return len(hashset) <= 1