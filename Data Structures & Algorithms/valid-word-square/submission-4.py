class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        matrix = []
        maxLen = len(max(words, key=len))
        for w in words:
            arr = []
            for ch in w:
                arr.append(ch)
            for i in range(len(arr), maxLen):
                arr.append(" ")
            matrix.append(arr)
        
        for r in range(len(words)):
            for c in range(len(words[r])):
                # Check if the 'transposed' index exists
                if c >= len(words) or r >= len(words[c]):
                    return False
                # Now it is safe to compare
                if words[r][c] != words[c][r]:
                    return False

        return True