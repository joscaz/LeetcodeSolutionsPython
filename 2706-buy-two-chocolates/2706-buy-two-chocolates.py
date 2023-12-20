class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()

        curr_money = money - prices[0]

        if money <= 0:
            return 0 
        
        curr_money -= prices[1]

        if curr_money >= 0:
            return curr_money
        else:
            return money