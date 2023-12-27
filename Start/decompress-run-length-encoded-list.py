class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list_to_return = []
        for num_ind in range(0, len(nums), 2):
            #adding the frequency of the element by list comrehension
            list_to_return.extend([nums[num_ind+1] for _ in range(nums[num_ind])])
        
        return  list_to_return