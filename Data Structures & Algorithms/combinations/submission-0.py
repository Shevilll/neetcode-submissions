class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, n, curr, comb, k):
            if len(curr) == k:
                comb.append(curr.copy())
                return
            
            if i == n + 1:
                return

            curr.append(i)

            helper(i + 1, n, curr, comb, k)

            curr.pop()

            helper(i + 1, n, curr, comb, k)

        
        comb = []

        helper(1, n, [], comb, k)

        return comb