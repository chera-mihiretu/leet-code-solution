class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                index = stack.pop()
                temp[index] = i - index
            stack.append(i)
        for i in stack:
            temp[i] = 0
        return temp
        
