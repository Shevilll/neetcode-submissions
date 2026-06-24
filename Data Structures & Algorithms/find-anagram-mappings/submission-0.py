class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums1:
            ans.append(nums2.index(i))

        return ans