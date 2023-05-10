from typing import List

def solution(mylist: List[List[int]]) -> List[int]:
    return [elem for array in mylist for elem in array]

mylist : List[List[int]] = [ [1], [2] ]
print(solution(mylist=mylist))