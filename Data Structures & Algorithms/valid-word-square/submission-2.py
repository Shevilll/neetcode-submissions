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
        
        k = 0
        while k < maxLen:
            for i in range(len(matrix[0])):
                if matrix[k][i] != matrix[i][k]:
                    return False
            k += 1

        return True