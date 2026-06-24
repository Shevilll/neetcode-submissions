class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_far = -1
        for i in range (len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_far
           # i = i-1
            max_far = max(max_far, temp)
        return arr    
        