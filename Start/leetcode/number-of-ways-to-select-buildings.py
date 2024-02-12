class Solution:
    def numberOfWays(self, s: str) -> int:
        one_number = defaultdict(int)
        two_comb = defaultdict(int)
        answer = 0
        for i in range(len(s)):
            #handle the three combination
            if s[i] == '0':
                answer += two_comb['1']
            else:
                answer += two_comb['0']

            #handle the two combination
            if s[i] == '0':
                two_comb[s[i]] += one_number['1']
            else:
                two_comb[s[i]] += one_number['0']
            
            #handle the one combination
            one_number[s[i]] += 1
        return answer
