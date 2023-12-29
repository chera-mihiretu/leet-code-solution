class Solution:
    def majorityElement(self, nums):
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                if len(freq) < 2:
                    freq[nums[i]] = 1
                else:
                    freq[nums[i]] = 1
                    li_pop = []
                    for i in freq.keys():
                        freq[i] -= 1
                        if freq[i] == 0:
                            li_pop.append(i)
                    for i in li_pop:
                        freq.pop(i)
        lis = []
        for i in freq.keys():
            if  nums.count(i) > len(nums)//3:
                lis.append(i)
        return lis
                
                
                    
            