class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter([0])
        summation = 0
        answer = 0
        for i in nums:
            summation += i
            rem = summation%k
            if rem in count:
                answer += count[rem]
            count[rem] += 1
        return answer



