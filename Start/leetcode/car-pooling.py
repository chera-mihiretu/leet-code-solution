class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_distance = 0
        for trip in trips:
            max_distance = max(max_distance, trip[2])
        prefix_sum = [0] * (max_distance + 2)
        for passenger, start, end in trips:
            prefix_sum[start] += passenger
            prefix_sum[end] -= passenger
        k = 0
        for i in prefix_sum:
            k += i
            if k > capacity:
                return False
        return True
