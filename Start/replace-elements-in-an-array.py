class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            num_hash[nums[i]] = i
        for num, replace in operations:
            index = num_hash[num]
            nums[index] = replace
            num_hash.pop(num)
            num_hash[replace] = index
        return nums