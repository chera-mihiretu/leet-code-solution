class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ha_1 = Counter(nums1)
        ha_2 = Counter(nums2)
        ret_li = []
        for i in ha_2:
            if i in ha_1:
                times = ha_2[i] if ha_2[i] < ha_1[i] else ha_1[i]
                ret_li.extend([i for _ in range(times)])
        return ret_li
                