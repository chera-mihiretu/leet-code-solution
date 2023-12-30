class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.distance = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, time = self.check_in[id]
        self.check_in.pop(id)
        if (check_in_station, stationName) in self.distance:
            self.distance[(check_in_station, stationName)].append(abs(t - time))
        else:
            self.distance[(check_in_station, stationName)] = [abs(t - time)]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.distance[(startStation, endStation)])/len(self.distance[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)