class Solution:
    def minimizedStringLength(self, s: str) -> int:
        element = []
        for i in range(len(s)):
            if not s[i] in element:
                element.append(s[i])
        return len(element)
