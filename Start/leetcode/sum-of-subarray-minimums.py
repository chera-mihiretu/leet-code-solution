class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9+7
        res = 0
        stack = []
        for ind, val in enumerate(arr):
            while stack and arr[stack[-1]] > arr[ind]:
                h_ind = stack.pop()
                left = h_ind - stack[-1] if stack else h_ind + 1
                right = ind - h_ind

                res += (arr[h_ind] * left * right)
            stack.append(ind)
        for i in range(len(stack)):
            left = stack[i] - stack[i-1] if i > 0 else stack[i] + 1
            right = len(arr) - stack[i]
            res += (arr[stack[i]] * left * right)


        return res % mod
