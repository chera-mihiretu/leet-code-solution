class Solution:
    def bestClosingTime(self, customers: str) -> int:
        offence = 0
        answer = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                offence -= 1
            else:
                offence += 1
            
            if offence < 0:
                answer = i + 1
                offence = 0

        return answer