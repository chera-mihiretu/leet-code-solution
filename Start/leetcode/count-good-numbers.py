class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (pow(10, 9) + 7)
        res, prime, even = 1,4,5
        even_pos = ceil(n / 2)
        odd_pos = n - even_pos

        res = pow(even, even_pos, MOD) * pow(prime, odd_pos, MOD)
        return res % MOD