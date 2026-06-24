class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            k = (l + r) // 2
            t = 0
            for i in piles:
                t += math.ceil(i / k)
            if t > h:
                l = k + 1
            else:
                r = k - 1
        return l