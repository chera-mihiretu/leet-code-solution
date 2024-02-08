class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete = set(nums)
        start = end = 0
        counter = Counter([nums[0]])
        answer = 0
        while end < len(nums):
            if counter.keys() == complete:
                answer += len(nums) - end
                counter[nums[start]] -= 1
                if counter[nums[start]] <= 0:
                    counter.pop(nums[start])
                if start == end:
                    if end < len(nums):
                        counter[nums[end]] += 1
                        end += 1
                start += 1
            else:
                end += 1
                if end < len(nums):
                    counter[nums[end]] += 1
        return answer
        

            
