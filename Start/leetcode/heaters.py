class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        answer = float('-inf')
        for i in range(len(houses)):
            result = bisect.bisect_right(heaters, houses[i])
            result = result % len(heaters)
            keep = min(abs(heaters[result]-houses[i]), abs(heaters[result-1]-houses[i]))
            answer = max(keep, answer)
        return answer
