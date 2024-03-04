class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        def subset(li):
            if not li:
                return
            answer.add(tuple(li))
            for i in range(len(li)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                subset(li[:i] + li[i+1:])
        subset(nums)

        answer.add(())

        return answer