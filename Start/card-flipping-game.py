class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cards = set()
        invalid = set()
        for i in range(len(fronts)):
            cards.add(backs[i])
            cards.add(fronts[i])
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])
        
        for i in invalid:
            if i in cards:
                cards.remove(i)
        if cards == set():
            return 0
        return min(cards)
