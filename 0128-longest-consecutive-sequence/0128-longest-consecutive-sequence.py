class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0

        for num in nums:
            # If true, then it's start of sequence
            if (num - 1) not in num_set:
                length = 0
                while (num+length) in num_set:
                    length += 1
                max_sequence = max(max_sequence, length)
        
        return max_sequence