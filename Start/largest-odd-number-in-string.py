class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if not int(num[i]) % 2:
                num = num[:i]
            else:
                return num
        return ""