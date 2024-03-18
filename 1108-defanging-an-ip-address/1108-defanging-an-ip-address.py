class Solution:
    def defangIPaddr(self, address: str) -> str:
        ad = address.replace('.', '[.]')
        return ad