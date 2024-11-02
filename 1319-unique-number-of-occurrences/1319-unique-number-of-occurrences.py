class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = defaultdict(int)

        for num in arr:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        return len(hm) == len(set(hm.values()))