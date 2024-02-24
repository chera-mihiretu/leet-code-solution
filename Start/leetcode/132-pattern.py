class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        next_large = -float('inf')
        for i in nums[::-1]:
            while stack and stack[-1] < i:
                x = stack.pop()
                next_large = max(next_large, x)
            if i < next_large:
                return True
            stack.append(i)
        return False