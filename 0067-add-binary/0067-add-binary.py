class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        suma = a + b

        suma_bin = bin(suma)

        return suma_bin[2:]