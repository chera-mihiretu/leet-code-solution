class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        no_count = Counter([cards[0]])
        start = end = 0
        max_present = 1
        min_size = float('inf')
        while end < len(cards):
            if max_present < 2:
                end +=1
                if end < len(cards):
                    no_count[cards[end]] +=1
                    max_present = max(no_count[cards[end]],  max_present)
            else:
                if no_count[cards[start]] == 2:
                    max_present -= 1
                no_count[cards[start]] -= 1
                start +=1
            if end < len(cards) and max_present ==2:
                min_size = min(min_size, end-start+1)
        return min_size if min_size != float('inf') else -1