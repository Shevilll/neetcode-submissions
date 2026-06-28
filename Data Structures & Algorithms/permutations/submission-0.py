class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            nextPerm = []
            for p in res:
                for j in range(len(p) + 1):
                    temp = p.copy()
                    temp.insert(j, i)
                    nextPerm.append(temp)

            res = nextPerm

        return res