class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashset = set(arr)

        count = 0

        for i in arr:
            if i + 1 in hashset:
                count += 1

        return count