class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        next_num = defaultdict(lambda: -1)
        stack = []
        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                index = stack.pop()
                next_num[index] = nums[i%n]
                
            stack.append(i%n)

        answer = []
        for i in range(n):
            answer.append(next_num[i])
        return answer