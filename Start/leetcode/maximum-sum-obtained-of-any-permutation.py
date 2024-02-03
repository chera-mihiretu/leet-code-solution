class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for start, end in requests:
            prefix_sum[start] += 1
            prefix_sum[end+1] -= 1
        k = 0
        for i in range(len(prefix_sum)):
            k += prefix_sum[i]
            prefix_sum[i] = k
        
        nums.sort(reverse=True)
        prefix_sum.sort(reverse=True)

        answer = 0
        for i in range(len(prefix_sum)-1):
            answer += prefix_sum[i] * nums[i]
        return answer % (pow(10, 9) + 7)

        
