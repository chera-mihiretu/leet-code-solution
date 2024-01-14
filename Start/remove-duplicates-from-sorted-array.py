class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        k = 0
        while right < len(nums):
            if not right == left:
                if nums[right] != nums[left-1]:
                    nums[right], nums[left] = nums[left], nums[right]
                    right += 1
                    left += 1
                    k += 1
                    continue
            if nums[left-1] >= nums[left]:
                right += 1
            else:
                right += 1
                left += 1
        return left
            