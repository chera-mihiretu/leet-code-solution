class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_for_plates = [0] * len(s)
        prefix_for_candle = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '|':
                prefix_for_plates[i] = prefix_for_plates[i-1] + 1
            else:
                prefix_for_plates[i] = prefix_for_plates[i-1]

            if s[i] == '*':
                prefix_for_candle[i] = prefix_for_candle[i-1] + 1
            else:
                prefix_for_candle[i] = prefix_for_candle[i-1]

            
        answer = []
        for start, end in queries:
            left_bound , right_bound = start, end
            if start - 1 >= 0 and prefix_for_plates[start - 1] == prefix_for_plates[start]:
                left_bound = bisect.bisect_left(prefix_for_plates, prefix_for_plates[start] + 1) 
            elif prefix_for_plates[start] == 0:
                left_bound = bisect.bisect_left(prefix_for_plates, 1)
            
            if end - 1 >= 0 and prefix_for_plates[end - 1] == prefix_for_plates[end]:
                right_bound = bisect.bisect_left(prefix_for_plates, prefix_for_plates[end])
            
            if left_bound >= right_bound:
                answer.append(0)
            else:
                answer.append(prefix_for_candle[right_bound] - prefix_for_candle[left_bound])

        return answer
