class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [float('-inf')] * n
        suffix = [float('-inf')] * n

        for i in range(n):
            prefix[i] = max(height[i], max(prefix[:i] if prefix[:i] else [0]))

        for i in range(n - 1, -1, -1):
            suffix[i] = max(height[i], max(suffix[i:] if suffix[i:] else [0]))

        total = 0

        for i in range(n):
            total += min(prefix[i], suffix[i]) - height[i]
        
        return total