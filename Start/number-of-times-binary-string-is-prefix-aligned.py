class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        prefix_count = {}
        tracker = 1
        answer = 0
        for i in range(len(flips)):
            prefix_count[flips[i]] = 1
            while tracker in prefix_count:
                prefix_count.pop(tracker)
                tracker += 1
            if len(prefix_count) == 0:
                answer += 1
        return answer
                