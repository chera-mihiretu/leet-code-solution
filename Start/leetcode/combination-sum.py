class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        def rec(li, an_li):
            if sum(an_li) == target:
                answer.add(tuple(sorted(an_li)))
                return
            if sum(an_li) > target:
                return 
            for i in range(len(li)):
                rec(li, an_li + [li[i]])
        rec(candidates, [])
        return answer

