class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _map = {}
        for i in range(len(names)):
            _map[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        li = []
        for i in heights:
            li.append(_map[i])
        return li
        