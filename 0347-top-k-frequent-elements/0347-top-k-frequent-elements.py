class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for i, v in count.items():
            freq[v].append(i)

        res = []

        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res