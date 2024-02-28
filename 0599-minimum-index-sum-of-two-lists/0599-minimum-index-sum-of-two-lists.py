class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm = {}
        ans = []
        minim = float("inf")

        for i in range(len(list1)):
            hm[list1[i]] = i
            
        for j in range(len(list2)):
            if list2[j] in hm:
                if minim > (j + hm[list2[j]]):
                    minim = (j + hm[list2[j]])
                    ans = [list2[j]]
                elif minim == (j + hm[list2[j]]):
                    ans.append(list2[j])
                else:
                    continue
        
        return ans
            