class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numbers = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        row = []
        start = 0
        for i in range(len(num1)-1, -1, -1):
            row.append("")
            row[-1] += " "*start
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                val = numbers[num1[i]] * numbers[num2[j]]
                val = val + carry
                carry = val//10
                val = val%10
                
                row[-1] = str(val) + row[-1] 
                if j-1 < 0 and carry!=0:
                    row[-1] = str(carry) + row[-1] 
            start += 1
        sum_str = ""
        carry = 0
        i = 1
        while i <= len(row[-1]):
            sum_col = 0
            for col in row:
                if i > len(col) or col[-i] == " ":
                    sum_col = sum_col + carry
                    carry=0
                else:
                    sum_col += numbers[col[-i]] + carry
                    carry=0
                    
            carry = sum_col // 10
            if  i+1 <= len(row[-1]):
                sum_col = sum_col%10
            sum_str = str(sum_col) + sum_str
            
            i+=1
        while sum_str != "0":
            if sum_str[0] == "0":
                sum_str = sum_str[1:]
            else:
                return sum_str
        return sum_str