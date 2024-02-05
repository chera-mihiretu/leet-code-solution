class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter({0: 1})
        result = t = 0
        for v in nums:
            t += v & 1
            result += counter[t - k]
            counter[t] += 1
        return result