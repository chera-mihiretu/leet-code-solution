class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        steps = 0
        for i in range(x+1):
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    steps += 1
                
                if i == k and tickets[k] == 0:
                    return steps
