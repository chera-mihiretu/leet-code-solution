class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_difference = 0
        for i in range(1, len(points)):
            max_difference = max(points[i][0]-points[i-1][0], max_difference)
        return max_difference