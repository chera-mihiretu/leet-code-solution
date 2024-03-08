class Solution:
    def hIndex(self, citations: List[int]) -> int:
        answer = 0
        start = 0
        end = len(citations) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if len(citations) - mid <= citations[mid]:
                answer = len(citations) - mid
                end = mid - 1
            else:
                start = mid + 1
        return answer

            