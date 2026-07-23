class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []

        for i, j in queries:
            temp = 0
            for k in range(i, j + 1):
                if words[k][0] in 'aeiou' and words[k][-1] in 'aeiou':
                    temp += 1

            ans.append(temp)

        return ans