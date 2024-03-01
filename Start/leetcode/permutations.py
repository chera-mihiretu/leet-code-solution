class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def perm(li, ans):
            if not li:
                answer.append(ans)
                return
            for i in range(len(li)):
                perm(li[:i] + li[i+1:], ans + [li[i]])
        perm(nums, [])
        return answer
