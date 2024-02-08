class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = end = 0
        sums = nums[0]
        max_sum = sums
        while end < len(nums):
            if sums < 0:
                end += 1
                start = end
                if end < len(nums):
                    sums = nums[end]
            else:
                end += 1
                if end < len(nums):
                    sums += nums[end]
            max_sum = max(sums, max_sum)
        return max_sum
        