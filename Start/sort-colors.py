class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min = nums[i]
            index = i
            for j in range(i+1, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    index = j
            if not index == i:
                nums[i], nums[index] = nums[index], nums[i]


        