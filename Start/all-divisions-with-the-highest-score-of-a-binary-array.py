class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = nums.count(1)
        highest = {right_sum:[0]}
        for i in range(len(nums)):
            if nums[i] == 0:
                left_sum+=1
            else:
                right_sum-=1
            sum_of = left_sum+right_sum
            for val in highest:
                if val < sum_of:
                    highest.popitem()
                    highest[sum_of] = [i+1]
                elif val == sum_of:
                    highest[sum_of].append(i+1)
        for i in highest:
            return highest[i]