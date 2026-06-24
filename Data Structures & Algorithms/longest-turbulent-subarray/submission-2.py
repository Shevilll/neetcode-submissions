class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        L = 0
        R = 1
        prev = ""

        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != ">":
                ans = max(ans, R - L + 1)
                prev = ">"
                R += 1
            elif arr[R - 1] < arr[R] and prev != "<":
                ans = max(ans, R - L + 1)
                prev = "<"
                R += 1
            else:
                if arr[R - 1] == arr[R]:
                    R += 1
                L = R - 1
                prev = ""
        return ans

