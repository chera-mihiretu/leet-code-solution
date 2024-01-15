class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        o_count = 0
        start = 0
        end = 0
        max_len = 0
        if nums[start] == 0:
            o_count = 1
        while end < len(nums):
            if o_count <= k:
                max_len = max(max_len, (end+1)-start)
                end += 1
                if end < len(nums) and nums[end] == 0:
                    o_count +=1
            else:
                if nums[start] ==0:
                    o_count -=1
                start += 1
                
                if o_count <= k:
                    max_len = max(max_len, (end+1)-start)
        return max_len
                
                    
                
                