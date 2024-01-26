class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        nums.append(0)
        
        for i in range(n):
            if nums[i-1] == nums[n-1] - nums[i]:
                return i
        return -1
                