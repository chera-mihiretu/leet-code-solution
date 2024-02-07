class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        start = end = 0
        total = nums[0]
        max_sum = 0
        count[nums[0]] += 1
        two_frequency = nums[0]
        while end < len(nums):
            if count[two_frequency] < 2:
                end += 1
                if end < len(nums):
                    count[nums[end]] += 1
                    if count[nums[end]] == 2:
                        two_frequency = nums[end]
                    total += nums[end]
            else:
                count[nums[start]] -= 1
                total -= nums[start]
                start += 1  
            if count[two_frequency] < 2:
                max_sum = max(max_sum, total)
        return max_sum

