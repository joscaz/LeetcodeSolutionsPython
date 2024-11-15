class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num, val in count.items():
            bucket[val].append(num)

        top_k = []

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                top_k.append(num)
                k -= 1
                if k == 0:
                    return top_k