class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [float('-inf')] * n
        suffix = [float('-inf')] * (n - 1)
        suffix.append(height[-1])

        for i in range(n):
            prefix[i] = max(height[i], prefix[i - 1])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i + 1])

        total = 0

        for i in range(n):
            total += min(prefix[i], suffix[i]) - height[i]
        
        return total