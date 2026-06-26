class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                return self.binarySearch(matrix[m], target)
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False