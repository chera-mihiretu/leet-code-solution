class Solution:
    def minimumSteps(self, s: str) -> int:
        swap_total = swap_for_each = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                swap_for_each += 1
            else:
                swap_total += swap_for_each
        return swap_total