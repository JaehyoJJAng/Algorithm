from typing import List
from itertools import permutations

def solution(mylist: List[int]) -> List[List[int]]:
    return sorted(list(permutations(mylist,len(mylist))))

mylist : List[int] = [2,1]
solution(mylist=mylist)