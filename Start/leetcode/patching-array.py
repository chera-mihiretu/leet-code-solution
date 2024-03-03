class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target = 0
        index = 0
        answer = 0
        while target < n:
            if index < len(nums) and nums[index] <= target + 1:
                target += nums[index]
                index += 1
            else:
                answer += 1
                target += target + 1
        return answer
            