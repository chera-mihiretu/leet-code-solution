class Solution:
    def escapeGhosts(self, ghosts, target):
        ghost_move = float("inf")

        #calculating the move for every ghost and store the shortest
        for ghost in ghosts:
            move_holder = abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            if ghost_move > move_holder:
                ghost_move = move_holder
        my_move = abs(0-target[0]) + abs(0-target[1])
        if my_move >= ghost_move:
            return False
        return True