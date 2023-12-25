class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ra = set()
        ra_1 = set()
        for i in ranges:
            for j in range(i[0], i[1]+1):
                ra.add(j)
        
        for i in range(left, right+1):
            ra_1.add(i)
        
        if not ra_1 - ra == set():
            return False
        else:
            return True
