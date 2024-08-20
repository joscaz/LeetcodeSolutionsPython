class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height)-1

        while i < j:
            base = j - i
            h = min(height[i], height[j])
            max_area = max(max_area, base*h)
            if height[i] < height[j] :
                i += 1
            else:
                j -= 1
            
        return max_area