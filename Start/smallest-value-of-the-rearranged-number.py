class Solution:
    def smallestNumber(self, num: int) -> int:
        li = []
        val = abs(num)
        val=str(val)
        li = list(val)
        li.sort(reverse=(num<0))
        if num < 0:
            value  = "".join(li)
            return -int(value)
        else:
            start = 0
            while start < len(li):
                if li[start] != '0':
                    li[start],li[0] = li[0],li[start]
                    break
                start += 1
            value = "".join(li)
            return int(value)
        