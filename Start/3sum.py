class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #answer container
        answer = set()
        used = set()
        for i in range(len(nums)):
            # current value
            if nums[i] == nums[i-1] and i != 0:
                continue
            val = nums[i]
            start = 0
            # searching for two number that could sum up to the currents values negative value
            end = len(nums) - 1
            
            while start < end:
                
                if start == i:
                    start +=1
                    continue
                if end == i:
                    end -= 1
                    continue
                    
                if nums[start] + nums[end] < -val:
                    start += 1
                elif nums[start] + nums[end] > -val:
                    end -= 1
                else:
                    triplets = tuple(sorted((val, nums[start], nums[end])))
                    answer.add(triplets)
                    start +=1 
                    end -= 1
        return  answer
                
            
            