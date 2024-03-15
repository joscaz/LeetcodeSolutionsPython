class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hm = {}
        i = 0

        for num in nums:
            if num not in hm:
                hm[num] = i
            else:
                if abs(hm[num] - i) <= k:
                    return True

                hm[num] = i

            i += 1

        return False