class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_picked = Counter([fruits[0]])
        start = end = 0
        answer = 1
        
        while end < len(fruits):
            if len(fruits_picked) <= 2:
                end += 1
                if end < len(fruits):
                    fruits_picked[fruits[end]] += 1
            else:
                fruits_picked[fruits[start]] -= 1
                if fruits_picked[fruits[start]] == 0:
                    fruits_picked.pop(fruits[start])
                start +=1 
            if end < len(fruits) and len(fruits_picked) <= 2:
                answer = max(answer, fruits_picked.total())
        return answer