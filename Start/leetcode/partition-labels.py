class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        length = len(s)
        answer_list = []
        _hash = {}
        for i in range(len(s)):
            if s[i] in _hash:
                _hash[s[i]][1] = i
            else:
                _hash[s[i]] = [i, -1]
        start = 0
        end = 0
        while start < len(s):
            if _hash[s[start]][1] == -1:
                answer_list.append(1)
                start +=1
            else:
                end = _hash[s[start]][1]
                hold = start + 1
                while hold < end:
                    if _hash[s[hold]][1] > end:
                        end = _hash[s[hold]][1]
                    hold += 1
                answer_list.append(end-start+1)
                start = end + 1
        return answer_list
            
                
                