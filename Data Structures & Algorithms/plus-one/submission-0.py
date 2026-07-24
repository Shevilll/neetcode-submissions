class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        i = len(digits) - 1
        while carry and i >= 0:
            digits[i] += carry
            if digits[i] > 9:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
            i -= 1

        if carry:
            digits.insert(0, 1)
        
        return digits