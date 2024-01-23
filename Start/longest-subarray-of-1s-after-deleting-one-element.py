class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 1 if nums[0] == 0 else 0
        start = end = 0
        max_len = 0
        while end  < len(nums):
            if zeros < 2:
                end += 1
                if end < len(nums) and nums[end] == 0:
                    zeros += 1
            else:
                if nums[start] == 0:
                    zeros -=1
                start += 1
            
            if zeros < 2 and end < len(nums):
                max_len = max(max_len, end - start)
        return max_len 