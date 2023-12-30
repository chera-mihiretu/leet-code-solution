class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        li = []
        sum_of_all = 0
        for i in nums:
            if not i %2:
                sum_of_all  += i
        
        for val, index in queries:
            if nums[index] % 2:
                if val % 2:
                    sum_of_all += nums[index] + val
            else:
                if val % 2:
                    sum_of_all -= nums[index]
                else:
                    sum_of_all += val
            nums[index] += val
            li.append(sum_of_all)
        return li