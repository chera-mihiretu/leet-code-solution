class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        distinct_element_count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                operations += distinct_element_count
            else:
                distinct_element_count += 1
                operations += distinct_element_count
        return operations
                