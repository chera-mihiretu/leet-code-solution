class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ha = {}
        for i in range(len(order)):
            ha[order[i]] = i
        for i in range(len(words)-1):
            a = 0
            b = 0
            while a <= len(words[i]) or b <= len(words[i+1]):
                if a >= len(words[i]):
                    break
                if b >= len(words[i+1]):
                    return False
                if ha[words[i][a]] > ha[words[i+1][b]]:
                    return False
                elif ha[words[i][a]] == ha[words[i+1][b]]:
                    pass
                else:
                    break
                a += 1
                b += 1
        return True