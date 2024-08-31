class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        curr = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > curr[1]:
                ans.append(curr)
                curr = [intervals[i][0], intervals[i][1]]
            
            elif curr[0] <= intervals[i][0] and curr[1] >= intervals[i][0]:
                curr = [min(intervals[i][0], curr[0]), max(intervals[i][1], curr[1])]
        
        ans.append(curr)
        
        return ans