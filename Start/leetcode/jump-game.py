class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            max_step = max(nums[i], max_step)
            if max_step == 0:
                return False
            max_step -= 1 
        return True

            


