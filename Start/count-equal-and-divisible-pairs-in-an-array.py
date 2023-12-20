class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ha = {}
        number = 0
        for i in range(len(nums)):
            if nums[i] in ha:
                for j in ha[nums[i]]:
                    if not (i*j)%k:
                        number += 1
                ha[nums[i]].append(i)
            elif not nums[i] in ha:
                ha[nums[i]] = [i]
        return number

