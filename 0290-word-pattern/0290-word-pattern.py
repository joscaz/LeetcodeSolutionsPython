class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        s = s.split(" ")
        i = 0
        if len(s) != len(pattern): return False
        if len(set(pattern)) != len(set(s)): return False

        for p in pattern:
            if p not in hm:
                hm[p] = s[i]

            elif hm[p] != s[i]:
                    return False

            i += 1

        return True
