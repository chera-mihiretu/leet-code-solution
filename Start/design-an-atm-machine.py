class ATM:

    def __init__(self):
        self.bank_notes = {}
        self.note_amount = [20, 50, 100, 200, 500]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        #depositing the money given
        for i in range(len(banknotesCount)):
            if banknotesCount[i] == 0:
                continue
            if self.note_amount[i] in self.bank_notes:
                self.bank_notes[self.note_amount[i]] += banknotesCount[i]
            else:
                self.bank_notes[self.note_amount[i]] = banknotesCount[i]
                
                
    def withdraw(self, amount: int) -> List[int]:
        #what to return
        deposited_notes = []
        #check for the type to remove
        for i in range(len(self.note_amount)-1, -1, -1):
            if self.note_amount[i] > amount:
                deposited_notes.insert(0,0)
                continue
            else:
                avilable_times = amount//self.note_amount[i]
                if not  self.note_amount[i] in self.bank_notes:
                    deposited_notes.insert(0,0)
                    continue
                #check if the avialable we can remove is in our atm
                while self.bank_notes[self.note_amount[i]] < avilable_times and self.bank_notes[self.note_amount[i]] != 0:
                    avilable_times = self.bank_notes[self.note_amount[i]]
                    
                # return if the atm dont have the note
                if self.bank_notes[self.note_amount[i]] == 0:
                    deposited_notes.insert(0,0)
                    continue
                amount = amount - (self.note_amount[i]*avilable_times)
                deposited_notes.insert(0,avilable_times)
                self.bank_notes[self.note_amount[i]] -= avilable_times
        #rolling back
        if amount != 0:
            for i in range(len(deposited_notes)):
                if deposited_notes[i] == 0:
                    continue
                if self.note_amount[i] in self.bank_notes:
                    self.bank_notes[self.note_amount[i]] += deposited_notes[i]
            return [-1]

        if amount == 0:
            return deposited_notes
                
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)