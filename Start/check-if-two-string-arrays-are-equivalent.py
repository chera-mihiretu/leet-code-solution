class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st = "".join(word1)
        st1 = "".join(word2)
        return st == st1
        