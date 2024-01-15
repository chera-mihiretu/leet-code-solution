class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans_occ = {'T':0, 'F':0}
        start = 0
        end = 0
        ans_occ[answerKey[0]] += 1
        max_cons = 0
        while end < len(answerKey):
            if min(ans_occ['T'], ans_occ['F']) <= k:
                end += 1
                if end < len(answerKey):
                    ans_occ[answerKey[end]] += 1
                if min(ans_occ['T'], ans_occ['F']) <= k:
                    max_cons = max(max_cons, ans_occ['T']+ans_occ['F'])
            else:
                start += 1
                ans_occ[answerKey[start-1]] -= 1
            
                
        return max_cons