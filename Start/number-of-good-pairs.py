class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        li = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    li.append((i, j))
        return len(li)


            
