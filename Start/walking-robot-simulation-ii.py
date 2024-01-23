class Robot:

    def __init__(self, width: int, height: int):
        self.height = height - 1
        self.width = width - 1
        self.cell = [0,0]
        self.dir_number = 0
        self.direction = ["East", "North", "West", "South"]
        self.available_box = height*width - (height-2) * (width-2)
        
    def step(self, num: int) -> None:
        
        num %= self.available_box
        if num == 0:
            if self.cell[0] == 0 and self.cell[1] == 0:
                self.dir_number = 3
              
        while num > 0:
            if self.dir_number == 0:
                if self.cell[0] + num > self.width:
                    num = (self.cell[0] + num) - self.width
                    self.cell[0] = self.width
                    self.dir_number += 1
                else:
                    self.cell[0] += num
                    num = 0
            if self.dir_number == 1:
                if self.cell[1] + num > self.height:
                    num =  (self.cell[1]  + num) - self.height
                    self.cell[1] = self.height
                    self.dir_number += 1
                else:
                    self.cell[1] += num
                    num = 0
            if self.dir_number == 2:
                if num - self.cell[0] > 0:
                    num = num - self.cell[0]
                    self.cell[0] = 0
                    self.dir_number += 1
                else:
                    self.cell[0] -= num
                    num = 0
            if self.dir_number == 3:
                if num - self.cell[1] > 0:
                    num = num - self.cell[1]
                    self.cell[1] = 0
                    self.dir_number += 1
                else:
                    self.cell[1] -= num
                    num = 0
            self.dir_number %= 4
        

    def getPos(self) -> List[int]:
        return self.cell
    

    def getDir(self) -> str:
        return self.direction [self.dir_number]
    
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()