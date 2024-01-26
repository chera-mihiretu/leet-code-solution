class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = end = 0
        who = 0
        while who < 2:
            if end >= len(nums):
                who +=1
                end = start
                continue
            if nums[end] == who:
                if end == start:
                    start += 1
                    end += 1
                else:
                    nums[start], nums[end] = nums[end],nums[start]
                    start +=1
                    end +=1
            else:
                end +=1

                



        