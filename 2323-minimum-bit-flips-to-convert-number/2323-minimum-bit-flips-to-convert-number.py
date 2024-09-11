class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        flips = 0

        # XOR - this operation will count if a bit is different, meaning there needs
        # to be a flip. 

        for i in range(len(bin(xor))):
            if bin(xor)[i] == '1':
                flips += 1

        return flips