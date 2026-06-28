class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, n, curr, comb, k):
            if len(curr) == k:
                comb.append(curr.copy())
                return
            
            if i == n + 1:
                return


            for j in range(i, n + 1):
                curr.append(j)

                helper(j + 1, n, curr, comb, k)

                curr.pop()

        
        comb = []

        helper(1, n, [], comb, k)

        return comb