class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        player = {}
        all_winners = []
        on_loser = []
        for i in matches:
            if not i[0] in player:
                player[i[0]] = 1
            if not i[1] in player:
                player[i[1]] = 1
            if i[0] in win:
                win[i[0]] += 1
            else:
                win[i[0]] = 1
            
            if i[1] in lose:
                lose[i[1]] +=1
            else:
                lose[i[1]] = 1
        for val, num in player.items():
            if not val in lose:
                all_winners.append(val)
            else:
                if lose[val] == 1:
                    on_loser.append(val)
        
        all_winners.sort()
        on_loser.sort()
        return [all_winners, on_loser]
                
