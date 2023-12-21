class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strts = ""
        while not word1 == "" and not word2 == "":
            strts += word1[0]
            strts += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        strts += word1+word2
        return strts