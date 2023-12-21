class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0
        for i in range(len(nums)):
            if i == 0 and nums[i] == 1:
                current = 1
                max = 1
                continue
            
            if nums[i] == 1 and nums[i-1] == 1:
                current += 1
                if max < current:
                    max = current
            elif nums[i] == 1:
                current = 1
                if max < current:
                   max = current
            else:
                current = 1
        return max