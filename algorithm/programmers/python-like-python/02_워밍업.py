from typing import List

def solution(mylist: List[List[int]]) -> List[int]:
    answer =  [len(length) for length in mylist]
    print(answer)

mylist : List[List[int]] = [[1],[2]]
solution(mylist=mylist)