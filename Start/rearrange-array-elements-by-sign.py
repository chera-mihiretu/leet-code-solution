class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        modified = []
        pos = 0
        neg = 0
        pick_pos = True
        while pos < len(nums) or neg < len(nums):
            if pick_pos:
                if pos >= len(nums):
                    pick_pos = not pick_pos
                    continue
                if nums[pos] > 0:
                    modified.append(nums[pos])
                    pos += 1
                    pick_pos = not pick_pos
                else:
                    pos += 1
            else:
                if neg >= len(nums):
                    pick_pos = not pick_pos
                    continue
                if nums[neg] < 0:
                    modified.append(nums[neg])
                    neg += 1
                    pick_pos = not pick_pos
                else:
                    neg +=1
        return modified 