class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        pre = nums[-1]
        answer = 0
        for i in range(len(nums)-2, -1,-1):
            if nums[i] <= pre:
                pre = nums[i]
            else:
                num_of_break = ceil(nums[i]/pre)
                answer += num_of_break - 1
                pre = nums[i]//num_of_break
        return answer

