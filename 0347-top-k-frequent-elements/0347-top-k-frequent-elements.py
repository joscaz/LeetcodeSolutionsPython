class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        
        for num, freq in hm.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
            
        return [v[1] for v in min_heap]
        
