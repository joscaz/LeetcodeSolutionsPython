class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        hm = {}

        for num in nums:
            if num not in hm:
                hm[num] = 0
                ans[hm[num]].append(num)
            
            elif hm[num] == len(ans):
                ans.append([])
                ans[hm[num]].append(num)
            
            else:
                ans[hm[num]].append(num)

            hm[num] += 1

        return ans