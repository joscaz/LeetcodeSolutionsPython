class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        for num, freq in hm.items():
            bucket[freq].append(num)
        
        top_k = []

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                top_k.append(num)
                k -= 1
                if k == 0:
                    return top_k