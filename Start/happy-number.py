class Solution:
    def isHappy(self, n: int) -> bool:
        ha ={}
        while True:
            n = str(n)
            holder = 0
            for i in n:
                holder += int(i)**2
            else:
                n = holder
                if n in ha:
                    return False
                else:
                    if n == 1:
                        return True
                    else:
                        ha[n] = 1
            