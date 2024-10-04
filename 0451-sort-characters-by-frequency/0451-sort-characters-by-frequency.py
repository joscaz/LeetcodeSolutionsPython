class Solution:
    def frequencySort(self, s: str) -> str:
        # bucket sort approach - o(n)
        hm = {}
        res = []

        for c in s:
            # can be written as hm[c] = 1 + hm.get(c, 0)
            if c not in hm:
                hm[c] = 0
            hm[c] += 1
        
        max_freq = max(hm.values())

        # initialize buckets
        # max_freq + 1 to include in case all chars are the same
        buckets = [[] for _ in range(max_freq+1)]

        for c, freq in hm.items():
            buckets[freq].append(c)
        
        for freq in range(max_freq, 0, -1):
            for c in buckets[freq]:
                res.append(c*freq)
        
        return ''.join(res)