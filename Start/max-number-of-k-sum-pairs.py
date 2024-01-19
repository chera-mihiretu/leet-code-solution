class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        pairs = 0
        while start < end:
            if k > nums[start] + nums[end]:
                start += 1
            elif k < nums[start] + nums[end]:
                end -= 1
            else:
                start += 1
                end -= 1
                pairs += 1
        return pairs