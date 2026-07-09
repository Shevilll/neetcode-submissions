class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        res = []

        for k, v in count.items():
            if v >= k:
                res.append(k)

        return res