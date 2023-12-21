class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        started = 0
        mid = 0
        end = 0
        for i in range(len(distance)):
            if i >= destination:
                end += distance[i]
            if i < start:
                started += distance[i]
               
            if i >= start and i < destination:
                mid += distance[i]
        return mid if mid < end+started else end+started
        
            
