class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = defaultdict(int)

        for num in arr:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        seen = set()

        for count in hm.values():
            if count in seen:
                return False
            seen.add(count)
        return True