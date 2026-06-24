class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = -1
        for key, value in count.items():
            if value == 1 and key > ans:
                ans = key

        return ans