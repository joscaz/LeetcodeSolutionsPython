class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution can be using heap or bucket sort

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        min_heap = []

        for num, freq in count.items():
            heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heappop(min_heap) # remove smallest frequency
        
        return [elem[1] for elem in min_heap]