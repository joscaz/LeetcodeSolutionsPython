class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        not_matched = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                not_matched += 1
            
        return not_matched