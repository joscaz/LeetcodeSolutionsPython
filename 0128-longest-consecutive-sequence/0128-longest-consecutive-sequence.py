class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        s = set(nums)

        for num in nums:
            # check if it's a starting sequence
            if (num - 1) not in s:
                cur_seq = 0
                while (num + cur_seq) in s:
                    cur_seq += 1
                max_seq = max(max_seq, cur_seq)
    
        return max_seq