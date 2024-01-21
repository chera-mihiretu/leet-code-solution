class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded  = set()
        guard_set = set()
        walls_set = set()
        def go_up(x,y):
            if x >= 0 and (x,y) not in guard_set and (x,y) not in walls_set:
                if (x,y) in unguarded:
                    unguarded.remove((x,y))
                go_up(x-1, y)
        def go_down(x,y):
            if x < m and (x,y) not in guard_set and (x,y) not in walls_set:
                if (x,y) in unguarded:
                    unguarded.remove((x,y))
                go_down(x+1, y)
                
        def go_right(x,y):
            if y < n and (x,y) not in guard_set and (x,y) not in walls_set:
                if (x,y) in unguarded:
                    unguarded.remove((x,y))
                go_right(x, y+1)
        def go_left(x,y):
            if y >= 0 and (x,y) not in guard_set and (x,y) not in walls_set:
                if (x,y) in unguarded:
                    unguarded.remove((x,y))
                go_left(x, y-1)
        for x, y in guards:
            guard_set.add((x,y))
        for x, y in walls:
            walls_set.add((x,y))
        for i in range(m):
            for j in range(n):
                if (i,j) not in walls_set  and (i,j) not in guard_set:
                    unguarded.add((i,j))
        #start the recursion here
        for x,y in guard_set:
            if (x,y) in unguarded:
                unguarded.remove((x,y))
            go_up(x-1,y)
            go_down(x+1,y)
            go_right(x,y+1)
            go_left(x,y-1)
        
        
        return len(unguarded)
    
        