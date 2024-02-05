class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_count = defaultdict(int)
        start = end = 0
        max_len = 0
        most_frequent = 0
        hash_count[s[0]] += 1
        while end < len(s):
            most_frequent = max(most_frequent, hash_count[s[end]])
            if (end - start + 1) - most_frequent <= k:
                max_len = max(max_len, end - start + 1)
                end += 1
                
                if end < len(s):
                    hash_count[s[end]] += 1
            else:
                hash_count[s[start]] -= 1
                start += 1
            
        return max_len
            
        