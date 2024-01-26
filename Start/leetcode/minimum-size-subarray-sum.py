class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        total = nums[0]
        min_len = float('INF') if nums[0] < target else 1
        while end < len(nums):
            if total <= target:
                end +=1
                if end < len(nums):
                    total += nums[end]
            else:
                if start == end:
                    return 1
                else:
                    total -= nums[start]
                    start += 1
            if total >= target and end < len(nums):
                min_len = min(min_len, end - start + 1)
        return min_len if min_len != float('inf') else 0
                    
                