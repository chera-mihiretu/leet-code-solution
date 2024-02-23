class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        array = []
        for i in range(len(weights)-1):
            array.append(weights[i]+weights[i+1])
        array.sort()

        max_val = sum(array[len(array)-k+1:])
        
        min_val = sum(array[:k-1])
        return max_val - min_val

        