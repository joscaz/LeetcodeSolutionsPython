class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for kid in candies:
            if kid + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output