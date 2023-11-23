class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        output = [False] * len(l)

        for i in range(len(l)):
            window = nums[l[i]:r[i]+1]
            window.sort()
            flag = False
            diff = window[1] - window[0]

            for j in range(1, len(window)):
                if window[j] - window[j - 1] == diff:
                    flag = True
                else:
                    flag = False
                    break
            
            if flag:
                output[i] = [True]
            
        return output