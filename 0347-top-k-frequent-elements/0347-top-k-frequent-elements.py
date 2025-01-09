class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int) # avoid key errors, value initialized to 0

        for num in nums:
            hm[num] += 1
        
        heap = []

        for num, val in hm.items():
            heappush(heap, (val, num))
            if len(heap) > k:
                heappop(heap)
        
        return [v[1] for v in heap]