class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        def subset(li):
            if not li:
                return
            if tuple(li) in answer:
                return
            answer.add(tuple(li))
            for i in range(len(li)):
                subset(li[:i] + li[i+1:])
        subset(nums)
        answer.add(())
        return answer