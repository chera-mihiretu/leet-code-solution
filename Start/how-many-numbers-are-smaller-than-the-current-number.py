class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append(0)
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    li[i] += 1
        return li
                