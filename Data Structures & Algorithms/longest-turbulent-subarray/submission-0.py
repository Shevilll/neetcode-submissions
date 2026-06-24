class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def test(a):
            first = True
            second = True
            for k in range(len(a) - 1):
                if k % 2 == 0:
                    if a[k] >= a[k + 1]:
                        first = False
                        break
                else:
                    if a[k] < a[k + 1]:
                        first = False
                        break

            for k in range(len(a) - 1):
                if k % 2 == 0:
                    if a[k] <= a[k + 1]:
                        second = False
                        break
                else:
                    if a[k] > a[k + 1]:
                        second = False
                        break
            return first or second

        L = 0
        ans = 0

        for R in range(len(arr)):
            if test(arr[L:R + 1]):
                ans = max(ans, R - L + 1)
            else:
                L += 1
            
        return ans