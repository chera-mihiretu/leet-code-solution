class Solution:
    def checkPossibility(self, nums) -> bool:
        times = 0
        i = 0 
        while i < len(nums)-1:
            
                
            if nums[i] > nums[i+1]:
                if i == 0:
                    if times > 0:
                        return False
                    times += 1
                    nums.pop(i)
                    continue
                if not nums[i-1] > nums[i+1]:
                    i -= 1
                if times > 0:
                    return False
                times += 1
                nums.pop(i+1)
      
                continue
            i+=1
        return True