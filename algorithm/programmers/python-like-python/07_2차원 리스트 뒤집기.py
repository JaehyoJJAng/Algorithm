from typing import List

def solution (mylist: List[List[int]]) -> None:
    # answer = []
    # for i in range(len(mylist)):
    #     answer.append([])        
    #     for j in range(len(mylist[i])):
    #         answer[i].append(mylist[j][i])
    # return answer    
    return list(map(list,zip(*mylist)))

mylist : List[List[int]] = [ [1,2,3], [4,5,6], [7,8,9] ]
solution(mylist=mylist)