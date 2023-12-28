class Solution:
    def wateringPlants(self, plants, capacity: int) -> int:
        move = 0
        water = capacity
        len(plants)
        for i in range(len(plants)):
            move += 1
            if water < plants[i]:
                move += (i)*2
                water = capacity
            
            water = water - plants[i]
            
            i=+1
        return move
                
                