class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key= lambda x: x[0])
        stack = []
        print(zipped)

        for i in range(len(zipped)):
            time = (target - zipped[i][0]) / zipped[i][1]
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)