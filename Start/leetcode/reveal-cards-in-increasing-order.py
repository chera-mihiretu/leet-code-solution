class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        print(deck)
        answer = deque()
        end = len(deck)-1
        for i in range(len(deck)-1, 0, -1):
            answer.appendleft(deck[i])
            answer.appendleft(answer.pop())
        answer.appendleft(deck[0])

        return list(answer)