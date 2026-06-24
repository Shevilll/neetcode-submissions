# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def mSort(arr, s, e):
            if (e - s + 1) <= 1:
                return
            m = (s + e) // 2
            mSort(arr, s, m)
            mSort(arr, m + 1, e)

            merge(arr, s, m, e)

        def merge(arr, s, m, e):
            l = s
            r = m + 1
            temp = s
            x = arr[:]
            while l <= m and r <= e:
                if arr[l].key <= arr[r].key:
                    x[temp] = arr[l]
                    l += 1
                else:
                    x[temp] = arr[r]
                    r += 1
                temp += 1
            
            if l <= m:
                while l <= m:
                    x[temp] = arr[l]
                    temp += 1
                    l += 1
            if r <= e:
                while r <= e:
                    x[temp] = arr[r]
                    temp += 1
                    r += 1
            temp = s
            while temp <= e:
                arr[temp] = x[temp]
                temp += 1

        mSort(pairs, 0, len(pairs) - 1)
        return pairs