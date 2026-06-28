class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            nextPrem = []
            for p in res:
                for j in range(len(p) + 1):
                    temp = p.copy()
                    temp.insert(j, i)
                    nextPrem.append(temp)
            res = nextPrem

        final = []

        for i in res:
            if i not in final:
                final.append(i)
        
        return final