class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hm = {}
        item_to_return = 0
        max_val = 0

        for num in nums:
            if num % 2 == 0:
                if num not in hm:
                    hm[num] = 0
                hm[num] += 1
        
        if len(hm) == 0:
            return -1
        
        for item in hm:
            if hm[item] > max_val:
                item_to_return = item
                max_val = hm[item]
            
            elif hm[item] == max_val:
                item_to_return = min(item, item_to_return)
        
        return item_to_return