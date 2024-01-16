class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        last = 0
        found_elements = {}
        element_to_contain = Counter(t)
        subs_list = []
        def add_to_found(index:int):
            if index < len(s):
                if s[last] in element_to_contain:
                    found_elements[s[last]] = found_elements.get(s[last], 0) + 1
        def check_fit():
            if element_to_contain.keys() == found_elements.keys():
                found_box = True
                for char, app in element_to_contain.items():
                    if app > found_elements[char]:
                        found_box = False    
                if found_box:
                    subs_list.append((start, last))
                return found_box
        while last < len(s):

            if start == last and s[start] not in element_to_contain:
                start += 1
                last += 1   
                check_fit()
            elif start ==  last:
                add_to_found(start)
                
                check_fit()
                last += 1
                add_to_found(last)
            else:
                while s[start] not in element_to_contain or (s[start] in found_elements and found_elements[s[start]] > element_to_contain[s[start]]):
                    if s[start] in element_to_contain:
                        found_elements[s[start]] -= 1
                    start += 1
                if s[last] in element_to_contain:  
                    if check_fit():
                        last += 1
                        add_to_found(last)
                    else:
                        last+= 1
                        add_to_found(last)
                else:
                    last+=1
                    add_to_found(last)
        check_fit()
        if subs_list == []:
            return ""
        ind = min(subs_list, key=lambda x: x[1] - x[0])
        return s[ind[0]:ind[1]+1]