from typing import List
def solution(mylist: List[List[int]]) -> List[int]:
    return list(map(len,mylist))

mylist : List[List[int]] = [ [1], [2] ]
print(solution(mylist=mylist))