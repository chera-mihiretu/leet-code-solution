class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_big = defaultdict(lambda: -1)
        stack = []
        for ind, val in enumerate(nums2):
            while stack and nums2[stack[-1]] < val:
                index = stack.pop()
                next_big[nums2[index]] = val
                
            stack.append(ind)
        answer = []

        for i in  nums1:
            answer.append(next_big[i])
        return answer
