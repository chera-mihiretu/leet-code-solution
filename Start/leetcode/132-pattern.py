class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        next_large = -float('inf')
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                x = stack.pop()
                next_large = max(next_large, x)
            if nums[i] < next_large:
                return True
            stack.append(nums[i])
        return False