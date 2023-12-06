class Solution:
    def totalMoney(self, n: int) -> int:
        mult = 1
        day = 1
        money = 1
        
        for i in range(1, n):
            if day == 7:
                mult += 1
                day = 1
            else:
                day += 1
            
            money = money + day + mult - 1
        
        return money
    
    # money = 1