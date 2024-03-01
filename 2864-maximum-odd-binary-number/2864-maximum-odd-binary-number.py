class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hm = {"0":0, "1":0}

        for digit in s:
            hm[digit]+=1
        
        new_string = ""
        hm["1"]-=1

        while hm["1"] != 0:
            new_string = "1" + new_string
            hm["1"] -= 1

        new_string = new_string + ("0"*(hm["0"]))

        return new_string + "1"