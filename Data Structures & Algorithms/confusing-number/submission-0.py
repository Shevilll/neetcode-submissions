class Solution:
    def confusingNumber(self, n: int) -> bool:
        while n:
            r = n % 10
            if r not in [0, 1, 9, 8, 6]:
                return False
            n //= 10

        return True