class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ha = {}
        for i in arr:
            if i in ha:
                ha[i] += 1
            else:
                ha[i]=1
        max = 0
        item = 0
        for i, values in ha.items():
            if max < values:
                max = values
                item = i
        return item