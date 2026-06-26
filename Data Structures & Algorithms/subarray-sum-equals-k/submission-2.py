class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}        
        p = []
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            p.append(pre)
            if pre in prefix:
                prefix[pre] += 1
            else:
                prefix[pre] = 1

        
        ans = 0
        for i in range(len(p)):
            if p[i] - k in prefix:
                ans += prefix[p[i] - k]
        
        return ans

