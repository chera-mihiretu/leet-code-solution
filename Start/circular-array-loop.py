class Solution:
    def circularArrayLoop(self, nums) -> bool:
        for i in range(len(nums)):
            index = set()
            start_index = i
            posative = False if nums[i] < 0 else True
            while i not in index:
                index.add(i)
                if nums[i] < 0 and posative: 
                    break
                elif nums[i] > 0 and not posative:
                    break
                i = (i + nums[i])%len(nums)
                
            if i == start_index and len(index) > 1:
                return True
        return False