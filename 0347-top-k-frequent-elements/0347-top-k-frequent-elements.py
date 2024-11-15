class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # +1 because there may be an element with the maximum frequency (len(nums)+1)
        freq = [ [] for i in range(len(nums) + 1)] 

        # count occurrences
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0 # initialize key
            count[num] += 1
        
        # add to bucket
        for i, v in count.items():
            freq[v].append(i)
        
        # iterate through bucket starting from end
        # the end contains the most freq elements

        res = [] # array with top k frq elements
        for i in range(len(nums), 0, -1):
            for elem in freq[i]:
                res.append(elem)
                k -= 1
                if k == 0:
                    return res