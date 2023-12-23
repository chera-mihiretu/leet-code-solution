class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li = []
        mx = max(candies)
        for i in candies:
            if i+extraCandies < mx:
                li.append(False)
            else:
                li.append(True)
        return li