class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ha = {}
        for i in strs:
            for j in range(len(strs[0])):
                if j in ha:
                    ha[j].append(i[j])
                else:
                    ha[j] = [i[j]]
        sumi  =0 
        for indx, items in ha.items():
            
            
            for i in range(len(items)-1):
                if items[i] > items[i+1]:
                    sumi += 1
                    break
        return sumi
                
                
                
            
                        