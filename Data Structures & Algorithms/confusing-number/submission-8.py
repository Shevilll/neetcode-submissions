class Solution:
    def confusingNumber(self, n: int) -> bool:
        res = 0
        temp = n
        hashmap = {0:0, 1:1, 6:9, 8:8, 9:6}
        while n:
            r = n % 10
            if r not in [0, 1, 9, 8, 6]:
                return False
            n //= 10
            res = res * 10 + hashmap[r]


        return res != temp