class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = ""
        end = 0
        for i in range(len(strs[0])):
            check = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]):
                    end = i
                    break
                if strs[j][i] != check:
                    end = i
                    break
            else:
                end = float("inf")
                continue
            break
        if end == float("inf"):
            end = len(strs[0])
        return strs[0][:end]





                