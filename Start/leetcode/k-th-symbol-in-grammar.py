class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        map = {'1':'10', '0':'01'}

        def goDeep(string, n, k):
            if n == 1:
                return string[k-1]
            power = 2**(n-1)
            if k > power:
                return goDeep(map[string[1]],n-1, k-power)
            else:
                return goDeep(map[string[0]], n-1, k)
        return int(goDeep('01', n, k))