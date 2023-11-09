class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            base = r - l
            min_height = min(height[l], height[r])
            area = base * min_height

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            
            elif height[l] > height[r]:
                r -= 1
            
            else:
                l += 1
                r -= 1

        return max_area