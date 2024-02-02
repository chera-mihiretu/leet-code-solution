class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = Counter([0, nums[0]])
        sub_arrays = 0
        if count[0] == 2 and goal == 0:
            sub_arrays = 1
        elif count[0] != 2 and goal == 1:
            sub_arrays = 1
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            diff = goal - nums[i]
            sub_arrays += count[-diff]
            count[nums[i]] += 1
        return sub_arrays

