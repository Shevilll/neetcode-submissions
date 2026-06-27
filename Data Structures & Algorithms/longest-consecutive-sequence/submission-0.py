class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        ans = 0

        for i in nums:
            if i - 1 not in nums:
                temp = 0
                x = i
                while x in s:
                    x += 1
                    temp += 1
                ans = max(ans, temp)

        return ans