class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swaped = set()
        start = 0
        end = 0
        while end < len(nums):
            if start == end:
                if nums[start] == val:
                   
                    end+= 1
                else:
                    start += 1
                    end+= 1
            else:
                if nums[start] == val:
                    if nums[end] != val:
                        nums[start],nums[end] = nums[end],nums[start]
                        start += 1
                        end += 1
                    else:
                        end += 1
                else:
                    start += 1
                    
                    
                
        return start
                    
                