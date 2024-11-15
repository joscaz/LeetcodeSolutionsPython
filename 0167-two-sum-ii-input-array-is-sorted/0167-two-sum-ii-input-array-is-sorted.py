class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            op = numbers[i] + numbers[j]
            if op == target:
                return [i+1, j+1]
            elif op > target:
                j -= 1
            else:
                i += 1