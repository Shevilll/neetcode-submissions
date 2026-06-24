class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic[target - val], i]
            dic[val] = i
        
        return [-1, -1]