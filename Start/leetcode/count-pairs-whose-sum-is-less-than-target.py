class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        start = 0
        nums.sort()
        end = len(nums) - 1
        answer = 0
        while start < end:
            if nums[start] + nums[end] < target:
                answer += (end - start)
                start += 1
            else:
                end -= 1
        return answer