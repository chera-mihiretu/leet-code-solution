class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        end = len(skill) - 1
        addition = None
        total = 0
        while start < end:
            if addition == None:
                addition = skill[start] + skill[end]
            else:
                if skill[start] + skill[end] != addition:
                    return -1
            total += skill[start] * skill[end]
            start += 1
            end -= 1
        return total