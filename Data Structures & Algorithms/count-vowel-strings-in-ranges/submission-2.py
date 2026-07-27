from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix = [0]

        for word in words:
            prefix.append(prefix[-1] + (word[0] in vowels and word[-1] in vowels))

        return [prefix[r + 1] - prefix[l] for l, r in queries]