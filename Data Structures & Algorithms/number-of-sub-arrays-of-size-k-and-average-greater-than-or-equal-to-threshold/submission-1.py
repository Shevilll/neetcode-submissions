class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        curr = sum(arr[:k - 1])
        for L in range(len(arr) - k + 1):
            curr += arr[L + k - 1]
            if curr / k >= threshold:
                ans += 1
            curr -= arr[L]
        
        return ans