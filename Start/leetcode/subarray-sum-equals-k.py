class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]*(len(nums)+1)
        count_prefix = Counter([0])
        total = 0
        
        for i in range(len(nums)):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]
            
            check = prefix_sum[i+1] - k
            if  check in count_prefix:
                total += count_prefix[check]
            count_prefix[prefix_sum[i+1]] += 1
        return total

