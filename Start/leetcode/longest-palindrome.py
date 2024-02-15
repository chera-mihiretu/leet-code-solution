class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd_count = 0
        for char, freq in count.items():
            if freq % 2:
                odd_count += 1
        return len(s) - (odd_count - 1 if odd_count != 0 else 0)
