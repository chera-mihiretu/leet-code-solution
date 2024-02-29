class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse= True)
        answer = 0

        for i in range(len(nums)-2):
            end_pt = len(nums) - 1
            for j in range(i+1, len(nums)-1):
                while nums[end_pt] + nums[j] <= nums[i]:
                    end_pt -= 1
                    if j >= end_pt:
                        break
                if j >= end_pt:
                    break

                answer += end_pt - j
        return answer

        