class Solution:
    def confusingNumber(self, n: int) -> bool:
        res = 0
        temp = n
        while n:
            r = n % 10
            if r not in [0, 1, 9, 8, 6]:
                return False
            n //= 10
            res = res * 10 + r

        return res != temp