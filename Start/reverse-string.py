class Solution:
    def reverseString(self, s: List[str]) -> None:
        x = len(s)
        for i in range(x//2):
            s[i], s[x-i-1] = s[x-i-1], s[i]
        