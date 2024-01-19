class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        new_set = nums1 & nums2
        return -1 if len(new_set) == 0 else min(new_set)
        