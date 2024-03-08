class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right, best = max(nums), sum(nums), -1
        answer = float('inf')
        while left <= right:
            mid = left + (right - left) // 2 
            cur_sum = 0
            partition = 1
            max_sum = 0
            
            for i in range(len(nums)):
                cur_sum += nums[i]
                if cur_sum > mid:
                    max_sum = max(cur_sum-nums[i], max_sum)
                    partition += 1
                    cur_sum = nums[i]
            max_sum = max(cur_sum, max_sum)
            if partition == k:
                answer = min(max_sum, answer)
                right = mid - 1
            elif partition < k:
                right = mid - 1
                answer = min(max_sum, answer)
            else:
                
                left = mid + 1

        return answer


