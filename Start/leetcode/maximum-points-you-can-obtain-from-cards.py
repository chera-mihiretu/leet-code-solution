class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        start = 0
        end = len(cardPoints) - (k+1)
        if end == -1:
            return sum(cardPoints)
        total = sum(cardPoints[-k:])
        x = len(cardPoints)
        max_total = total
        while end < x:
            start += 1
            end += 1
            total += cardPoints[start-1]
            if end < x:
                total -= cardPoints[end]
                max_total = max(max_total, total)
        return max_total