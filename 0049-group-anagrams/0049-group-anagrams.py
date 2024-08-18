class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in range(len(strs)):
            hm[i] = {}
            for letter in strs[i]:
                if letter not in hm[i]:
                    hm[i][letter] = 0
                hm[i][letter] += 1
        
        '''
        {0: {7}, 1: {13}, 
        2: {'t': 1, 'a': 1, 'n': 1}, 3: {16}, 
        4: {'n': 1, 'a': 1, 't': 1}, 5: {'b': 1, 'a': 1, 't': 1}}

        curr = [] -> curr = [eat]
        hm[0]==hm[j] --> curr = [eat, tea]
        hm[0] = {14} j+=1
        hm[0] == hm[3] --> curr = [eat, tea, ate]
        hm[3] = {16}
        hm[0] = {7}
        
        '''

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