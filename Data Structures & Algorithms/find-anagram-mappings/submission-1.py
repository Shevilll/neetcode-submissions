class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1) 
        hashmap = {}

        for k, v in enumerate(nums2):
            hashmap[v] = k

        
        for k, v in enumerate(nums1):
            ans[k] = hashmap[v]

        return ans