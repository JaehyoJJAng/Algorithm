from typing import List

def solution(mylist: List[int]) -> List[int]:
    # answer = []
    # for i in range(len(mylist) - 1):        
    #     return answer.append(abs(mylist[i] - mylist[i + 1]))
    
    answer : List[int] = [abs(mylist[i] - mylist[i + 1]) for i in range(0,len(mylist) - 1)]
    return answer

mylist : List[int] = [83, 48, 13, 4, 71, 11]
solution(mylist=mylist)