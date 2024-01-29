class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        answer = []
        while end > 1:
            index = arr.index(end)
            if index != 0 and index != end-1:
                arr[:index+1] = arr[index::-1]
                answer.append(index+1)
            if index != end-1:
                arr[:end] = arr[end-1::-1]
                answer.append(end)
            end -=1
        return answer