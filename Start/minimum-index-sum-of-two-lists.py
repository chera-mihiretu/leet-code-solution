class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {}
        l2 = {}
        l_sum = {}
        x = len(list1) if len(list1) > len(list2) else len(list2)
        for i in range(x):
            if i < len(list1):
                l1[list1[i]]=i
                
            if i < len(list2):
                l2[list2[i]] = i
        
        for v, ind in l1.items():
            if v in l2:
                l_sum[v] = ind+l2[v]
        mini = float('inf')
        val = []
        print (l_sum)
        for value, ind in l_sum.items():
            if ind < mini:
                mini = ind
                val = [value]
            elif ind == mini:
                val.append(value)
        return val
        