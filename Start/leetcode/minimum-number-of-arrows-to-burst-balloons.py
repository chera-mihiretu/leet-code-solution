class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        min_val = points[0][1]
        arrow_needed = 1
        for start, end in points[1:]:
            if min_val < start:
                arrow_needed += 1
                min_val = end
            else:
                min_val = min(min_val, end) 
            
        return arrow_needed


