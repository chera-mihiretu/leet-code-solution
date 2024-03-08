class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_interval = sorted(intervals)
        indexes = {(start, end) : i for i , (start, end) in enumerate(intervals)}

        for index, (start, end) in enumerate(intervals):
    
            ind = bisect.bisect_left(new_interval, [end])
            if ind < len(new_interval):
                intervals[index] = indexes[tuple(new_interval[ind])]
            else:
                intervals[index] = -1



        return intervals
        