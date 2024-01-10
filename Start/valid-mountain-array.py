class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr)-1
        if len(arr) ==2:
            return False
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                i+=1
            else:
                break
        while j > 0:
            if arr[j] < arr[j-1]:
                j-=1
            else:
                break
        if   j == len(arr)-1 or i == 0:
            return False
        if i == j:
            return True
        elif j-1 == i and arr[j] != arr[i]:
            return False
            
            
        
            
            
            