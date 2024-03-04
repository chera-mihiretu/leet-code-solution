class Solution(object):
    def letterCombinations(self, digits):
        letters = {"2":["a","b","c"],"3":["d","e","f"], "4":["g","h","i"],
        "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],"8":["t","u","v"]
        , "9":["w","x","y","z"]}
        answer = []
        def com(indx, li):
            if len(li) == len(digits):
                if li:
                    answer.append(''.join(li))
                return
            for i in letters[digits[indx]]:
                com(indx+1, li+[i])
        com(0, [])
        return answer
            


        