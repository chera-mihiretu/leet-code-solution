# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        answer  = float('inf')
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            value =  isBadVersion(mid)
            if value:
                answer = min(mid, answer)
                right = mid - 1
            else:
                left = mid + 1
        return answer
            