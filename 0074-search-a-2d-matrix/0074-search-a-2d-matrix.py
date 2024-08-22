class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix)-1

        while i <= j:
            mid = (i + j) // 2

            if target in matrix[mid]:
                return True
            
            elif matrix[mid][0] > target:
                j = mid - 1

            else:
                i = mid + 1
        return False