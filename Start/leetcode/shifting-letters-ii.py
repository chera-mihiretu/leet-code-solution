class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * len(s)
        for start, end, forward in shifts:
            forward = -1 if forward == 0 else 1
            arr[start] +=  forward
            if end+1 < len(arr):
                arr[end+1] -= forward
        s = list(s)
        k = 0
        for i in range(len(s)):
            k+=arr[i]
            s[i] = chr((((ord(s[i]) - ord('a')) + k) % 26) + ord('a'))
        return "".join(s)