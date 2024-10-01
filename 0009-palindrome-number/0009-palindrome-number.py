class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)

        i, j = 0, len(num_str) - 1

        while i<=j:
            if num_str[i] != num_str[j]:
                return False
            i += 1
            j -= 1
        
        return True