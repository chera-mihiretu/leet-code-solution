class Solution:
    def average(self, salary: List[int]) -> float:
        mini = float("inf")
        maxx = 0
        summ = 0
        for i in salary:
            summ += i
            if mini > i:
                mini = i
            if maxx < i:
                maxx = i
        print(mini, maxx)
        summ = float((summ - (mini + maxx))/(len(salary)-2))
        return summ
        