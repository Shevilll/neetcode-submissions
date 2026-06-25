class Solution:
    def trap(self, height: List[int]) -> int:
        def findMax(i):
            lmax, rmax = float('-inf'), float('-inf')
            l = i - 1
            r = i + 1
            while l >= 0:
                lmax = height[l] if height[l] > height[i] and height[l] > lmax else lmax
                l -= 1
            while r < len(height):
                rmax = height[r] if height[r] > height[i] and height[r] > rmax else rmax
                r += 1
            return lmax, rmax

        
        total = 0

        for i in range(len(height)):
            lmax, rmax = findMax(i)
            if lmax == float('-inf') or rmax == float('-inf') or not lmax or not rmax:
                continue
            total += min(lmax, rmax) - height[i]
        
        return total