class FrequencyTracker:

    def __init__(self):
        self.hash = {}
        self.frequency_val = {}

    def add(self, number: int) -> None:
        if number in self.hash:
            self.frequency_val[self.hash[number]].remove(number)
            if self.frequency_val[self.hash[number]] == set():
                self.frequency_val.pop(self.hash[number])
            self.hash[number] += 1
            
        else:
            self.hash[number] = 1
        
        if self.hash[number] in self.frequency_val:
            self.frequency_val[self.hash[number]].add(number)
        else:
            self.frequency_val[self.hash[number]] = set([number])

            
    def deleteOne(self, number: int) -> None:
        if number in self.hash:
            self.frequency_val[self.hash[number]].remove(number)
            if self.frequency_val[self.hash[number]] == set():
                self.frequency_val.pop(self.hash[number])
            if self.hash[number] == 1:
                self.hash.pop(number)
            else:
                self.hash[number] -= 1
        else:
            return
        if number not in self.hash:
            return
        if self.hash[number] in self.frequency_val:
            self.frequency_val[self.hash[number]].add(number)
        else:
            self.frequency_val[self.hash[number]] = set([number])
        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency_val:
            return True
        return False