class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ha = {}
        for i in nums:
            ha[i] = [1]
        for i in range(len(nums)+1):
            if not i in ha:
                return i