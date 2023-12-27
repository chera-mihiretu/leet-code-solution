class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if a+b > c and c+a > b and b+c > a:
                return a+b+c
        if len(nums) <= 3:
            a = nums[0]
            b = nums[1]
            c = nums[2]
            if a+b > c and c+a > b and b+c > a:
                return a+b+c
        return 0
                        

            