class Solution(object):
    def twoSum(self, nums, target):
        ha ={}
        for i in range(len(nums)):
            if nums[i] in ha:
                return [i, ha[nums[i]]]
            else:
                ha[target - nums[i]] = i


        