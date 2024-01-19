class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        counter = Counter()
        longer = 0
        while end < len(s):
            if counter[s[end]] == 1:
                counter[s[start]] -= 1
                start += 1
            else:
                counter[s[end]] += 1
                
                longer = max(longer, end-start+1)
                end += 1
        return longer