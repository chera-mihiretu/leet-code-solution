class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for val, freq in count.items():
            if not freq % (val+1):
                total += freq
            else:
                total += (freq//(val+1)*(val+1)) + (val+1)
        return total