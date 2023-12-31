class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[len(digits)-(i+1)] !=9:
                digits[len(digits)-(i+1)] += 1
                break
            else: 
                if i+1 == len(digits):
                    digits.insert(0,1)
                digits[len(digits)-(i+1)] = 0
        return digits
        