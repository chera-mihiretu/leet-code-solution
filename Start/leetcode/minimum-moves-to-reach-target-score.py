class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while maxDoubles > 0:
            if target == 1:
                return steps
            if not target  % 2:
                target //= 2
                steps += 1
                maxDoubles -= 1
            else:
                steps += 1
                target -= 1

        return steps + target - 1
            
