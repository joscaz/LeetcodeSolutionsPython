class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            if target in matrix[mid]:
                return True
            elif target > matrix[mid][len(matrix)-1]:
                low = mid + 1
            else:
                high = mid - 1
        
        return False