class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        min_val = 0
        for i in range(0, len(tasks), 4):
            max_of_four = 0 
            for j in range(4):
                max_of_four = max(max_of_four, processorTime[i//4] + tasks[i+j])
            min_val = max(min_val, max_of_four)
            
        return min_val