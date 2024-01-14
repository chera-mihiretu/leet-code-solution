class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        li = []
        for i in s:
            if ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 48 and ord(i) <= 57:
                li.append(i)

        for i in range(len(li)//2):
            if li[i] != li[-(i+1)]:
                return False
        
        return True            