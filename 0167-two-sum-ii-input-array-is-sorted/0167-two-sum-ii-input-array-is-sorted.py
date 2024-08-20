class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        

        while i < j:
            addition = numbers[i] + numbers[j]
            if addition == target:
                return [i+1, j+1]
            elif addition < target:
                i += 1
            
            elif addition > target:
                j -= 1