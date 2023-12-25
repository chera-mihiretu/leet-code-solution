class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ha = {}
        str_1 = ""
        for i in range(len(s)):
            ha[indices[i]] = s[i]
        for i in range(len(s)):
            str_1 += ha[i]
        return str_1