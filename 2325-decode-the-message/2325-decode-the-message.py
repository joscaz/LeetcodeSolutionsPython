class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        numLetter = 1
        ans = ""
        
        hm = {}
        
        # mapping each letter to the alphabet
        for letter in key:
            if letter == " ":
                continue
            elif letter not in hm:
                hm[letter] = alphabet[numLetter-1]
                numLetter += 1
                
        #decode message
        for letter in message:
            if letter == " ":
                ans += " "
            
            else:
                ans += hm[letter]
        
        return ans