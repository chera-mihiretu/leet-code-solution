class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def comb(li, k):
            if not k:
                answer.append(li)
                return
            next = li[-1] + 1 if li else 1
            for i in range(next, n+1):
                comb(li+[i], k-1)
        comb([], k)
        return answer