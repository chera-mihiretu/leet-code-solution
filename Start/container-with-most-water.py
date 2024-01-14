class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        last = len(height) - 1
        start = 0
        while start < last:
            area = max(area, (last - start) * min(height[start] , height[last]))
            if height[start] < height[last]:
                start += 1
            else:
                last -= 1
        return area
            