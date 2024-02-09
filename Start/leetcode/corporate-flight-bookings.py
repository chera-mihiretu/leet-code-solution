class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n+1)
        for start, end, seat in bookings:
            prefix_sum[start-1] += seat
            prefix_sum[end] -= seat
        k = 0
        for i in range(len(prefix_sum)):
            k +=  prefix_sum[i]
            prefix_sum[i] = k
        return prefix_sum[:-1]
