class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        li = []
        for box in range(len(boxes)):
            su = 0
            for ball in range(len(boxes)):
                if ball == box:
                    continue
                if boxes[ball] == "1":
                    su += abs(ball - box)
                else:
                    continue
            li.append(su)
        return li