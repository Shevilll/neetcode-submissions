class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two   #one,two = one + two
            two = temp
        return one       # TM O(n)
        

















    
        # if n <= 2:
        #     return n

        # return self.climbStairs(n-1)+self.climbStairs(n-2)    TM = O(2^n)    
        