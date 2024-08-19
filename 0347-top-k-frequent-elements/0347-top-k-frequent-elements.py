class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        ans = []
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        '''{1:3, 2:2, 3:1}'''

        bucket = {i: [] for i in range(len(nums)+1)}

        for i, v in hm.items():
            bucket[v].append(i)
        
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                    ans.append(bucket[i][j])
                    k -= 1
                if k == 0:
                    return ans

        return ans