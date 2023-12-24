class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greator = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greator.append(i)
            else:
                equal.append(i)
        return less+equal+greator