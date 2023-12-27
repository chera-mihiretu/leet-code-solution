class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list_numbers = {}
        for i in nums:
            list_numbers[i] =1

        pop_count = 0
        max_pop_count= 0
        while list_numbers != {}:
            value = list_numbers.popitem()[0]
            list_numbers[value] = 1
            pop_count = 0
            while value-1 in list_numbers:
                value -= 1
                
            while value in list_numbers:
                list_numbers.pop(value)
                value = value+1
                pop_count += 1
            
            if max_pop_count < pop_count:
                max_pop_count = pop_count
        return max_pop_count
                
                
                
        
                
            
            
