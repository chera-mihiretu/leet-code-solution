class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li = []
        for i in range(n):
            li.append(nums[i])
            li.append(nums[n+i])
        return li