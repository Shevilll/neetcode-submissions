class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        ans = []
        temp = 0
        for i in count:
            if temp != k:
                ans.append(i[0])
                temp += 1

        return ans
