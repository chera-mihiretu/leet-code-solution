class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        max_average = -float('inf')
        total = nums[0]
        while end < len(nums):
            if end - start < k-1:
                end += 1
                total += nums[end]
            else:
                if start != 0:
                    total -= nums[start-1]
                    total += nums[end]
                max_average = max(max_average, total/k)
                
                start += 1
                end += 1
        return max_average
                