class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        {}
        '''

        hm = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s)-ord('a')] += 1
            
            hm[tuple(count)].append(word)
    
        return list(hm.values())