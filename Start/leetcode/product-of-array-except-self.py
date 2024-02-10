class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in nums:
            left.append(left[-1]*i)
        for i in nums[:0:-1]:
            right.append(right[-1]*i)
        answer = []
        right.reverse()
        for i in range(len(nums)):
            answer.append(left[i]*right[i])
        return answer       
        

