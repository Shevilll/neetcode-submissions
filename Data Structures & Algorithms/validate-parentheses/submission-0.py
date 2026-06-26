class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack  == []:
                    return False


                if stack[-1] in "([{":    
                    stack.pop()

                else :
                    return False
        return stack == []                      
                
       