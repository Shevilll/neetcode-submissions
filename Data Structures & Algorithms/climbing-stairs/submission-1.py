class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        def fib(n):
            if n == 0 or n == 1:
                return n
            if n in dic:
                return dic[n]
            
            k = fib(n - 1) + fib(n - 2)
            dic[n] = k
            return k
        return fib(n + 1)