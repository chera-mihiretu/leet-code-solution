class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        start, end = 0, len(nums) - 1
        minimum = nums[0]
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= minimum:
                minimum = nums[mid]
                start  = mid + 1
            elif nums[mid] < minimum:
                end = mid - 1
        return nums[start]

            
