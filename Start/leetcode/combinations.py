class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(depth, li):
            if depth == k:
                answer.append(li)
                return
            start = li[-1] + 1 if li else  1
            for i in range(start, n + 1):
                dfs(depth + 1, li + [i])
        dfs(0, [])
        return answer