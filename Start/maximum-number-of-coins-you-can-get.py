class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = len(piles)//3
        total =0 
        for i in range(start, len(piles), 2):
            total += piles[i]
        return total