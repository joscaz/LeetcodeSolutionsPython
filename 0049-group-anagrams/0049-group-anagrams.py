class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in range(len(strs)):
            hm[i] = {}
            for letter in strs[i]:
                if letter not in hm[i]:
                    hm[i][letter] = 0
                hm[i][letter] += 1

        ans = []
        for i in range(len(strs)):
            curr = []
            if hm[i] != 0:
                curr.append(strs[i])
                for j in range(i+1, len(strs)):
                    if hm[i] == hm[j] and hm[j] != 0:
                        curr.append(strs[j])
                        hm[j] = 0
                ans.append(curr)
        return ans