class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float("inf")
        for number in nums:
            if number <= i:
                i = number
            elif number <= j:
                j = number
            else:
                return True
        return False
            
        
                    
                
                 