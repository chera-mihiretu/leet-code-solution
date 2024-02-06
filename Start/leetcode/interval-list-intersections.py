class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_pointer = 0
        second_pointer = 0
        answer = []
        while first_pointer < len(firstList) and second_pointer < len(secondList):
           
            if firstList[first_pointer][0] >= secondList[second_pointer][0]:
                if firstList[first_pointer][0] > secondList[second_pointer][1]:
                    second_pointer += 1
                    continue
                elif firstList[first_pointer][0] == secondList[second_pointer][1]:
                    answer.append([firstList[first_pointer][0], firstList[first_pointer][0]])
                    second_pointer += 1
                elif firstList[first_pointer][1] <= secondList[second_pointer][1]:
                    answer.append(firstList[first_pointer])
                    first_pointer += 1
                else:
                    answer.append([firstList[first_pointer][0], secondList[second_pointer][1]])
                    second_pointer+= 1
                
            else:
                if secondList[second_pointer][0] > firstList[first_pointer][1]:
                    first_pointer += 1
                    continue
                elif secondList[second_pointer][0] == firstList[first_pointer][1]:
                    answer.append([firstList[first_pointer][1], firstList[first_pointer][1]])
                    first_pointer += 1
                elif firstList[first_pointer][1] >= secondList[second_pointer][1]:
                    answer.append(secondList[second_pointer])
                    second_pointer += 1
                else:
                    answer.append([secondList[second_pointer][0],firstList[first_pointer][1]])
                    first_pointer += 1
            #print (first_pointer, second_pointer)
        return answer