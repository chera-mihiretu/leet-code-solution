class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        output = 0
        while start <= end:
            if start == end:
                output += 1
                start +=1
                continue
            if people[start] + people[end] <= limit:
                start +=1
                end -=1
                output += 1
            else:
                end -= 1
                output += 1
        return output