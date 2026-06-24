class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0, 1]

        i = 1
        while i <= n:
            temp = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = temp
            i += 1
        
        return fib[1]
