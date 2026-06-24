class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        for L in range(len(arr)):
            if L + k > len(arr):
                return ans
            if (sum(arr[L:L+k]) / k) >= threshold:
                ans += 1
        
        return ans