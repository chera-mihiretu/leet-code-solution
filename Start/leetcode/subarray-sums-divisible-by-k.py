class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_rem = Counter([0])
        result = 0
        for i in range(len(nums)):
            if i != 0:
                nums[i] = nums[i] + nums[i-1]
            if nums[i] % k in count_rem:
                result += count_rem[nums[i] % k]
            
            count_rem[nums[i] % k] +=1
        
        return result

