class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        j = 1
        ret = [""]
        while i < len(num) and j < len(num):
            if num[i] == num[j]:
                if (j - i) == 2:
                    ret.append(num[i:j+1])
                j+=1
            else:
                i = j
                j +=1

        return max(ret)