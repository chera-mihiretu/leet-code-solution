class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        letters = ["Q", "W", "E", "R"]
        #find the content
        for i in letters:
            if i not in count:
                continue
            if count[i] <= (len(s)/4):
                count.pop(i)
            else:
                count[i] -= (len(s)//4)
        #sliding windoe
        start = end = 0
        new_count = Counter(s[0])
        min_len = float('inf')
        if count == Counter():
            return 0
        while end < len(s):
            if count - new_count == Counter():
                min_len = min(min_len, end-start+1)
                new_count[s[start]] -= 1
                if end == start:
                    end+=1
                    if end < len(s):
                        new_count[s[end]] += 1
                start += 1
            else:
                end += 1
                if end < len(s):
                    new_count[s[end]] += 1
            

            

            
        return min_len
