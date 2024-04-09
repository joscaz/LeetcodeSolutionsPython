class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        idx = 0
        seconds = 0
        while tickets[k] > 0:
            if idx == len(tickets):
                idx = 0
            
            if idx == k:
                tickets[k] -= 1
                seconds += 1

            elif tickets[idx] > 0:
                tickets[idx] -= 1
                seconds += 1
            
            idx += 1
        
        return seconds