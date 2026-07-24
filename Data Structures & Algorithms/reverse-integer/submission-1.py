class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1

        x = str(abs(x))[::-1]

        if int(x) in range(-2**31, 2**31):
            return int(x) if flag == 0 else -int(x)
        
        return 0
        