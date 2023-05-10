from typing import List
def solution(mylist: List[List[int]]) -> List[int]:
    return list(map(int,mylist))

mylist : List[List[int]] = [ [1], [2] ]
solution(mylist=mylist)