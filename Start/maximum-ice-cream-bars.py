class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        start = 0
        #the money he spend at every bar 
        total = 0
        # the ice cream he boughts
        ice_creams = 0
        while total < coins and start < len(costs):
            total += costs[start]
            if total <= coins:
                ice_creams +=1
            start +=1
            
       
        return ice_creams
            