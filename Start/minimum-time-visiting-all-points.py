class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i,j = points[0]
        moves = 0
        for point in points[1:]:
            while not(i == point[0] and j == point[1]):
                if i < point[0]:
                    i += 1
                elif i > point[0]:
                    i -= 1
                if j < point[1]:
                    j += 1
                elif j > point[1]:
                    j -= 1
                moves += 1
        return moves
                