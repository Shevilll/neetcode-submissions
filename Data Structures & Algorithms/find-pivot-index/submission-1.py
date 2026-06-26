class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        postfix = []
        pre = 0
        pos = 0
        for i in range(len(nums)):
            pre += nums[i]
            prefix.append(pre)
            pos += nums[len(nums) - i - 1]
            postfix.append(pos)

        postfix.reverse()
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i

        return -1