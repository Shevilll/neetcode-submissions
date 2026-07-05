class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        temp = []

        for s in strs:
            zeroes, ones = 0, 0
            for c in s:
                if c == '0': zeroes += 1
                if c == '1': ones += 1
            temp.append([zeroes, ones])

        

        def dfs(i, curr_m, curr_n):
            if i >= len(strs): return 0

            skip = dfs(i + 1, curr_m, curr_n)
            if curr_m - temp[i][0] >= 0 and curr_n - temp[i][1] >= 0:
                take = 1 + dfs(i + 1, curr_m - temp[i][0], curr_n - temp[i][1])
                return max(skip, take)

            return skip

        return dfs(0, m, n)

