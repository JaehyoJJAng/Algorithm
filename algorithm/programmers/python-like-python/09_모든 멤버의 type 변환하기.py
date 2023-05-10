from typing import List

def solution(mylist: List[str]) -> List[int]:
    # return [int(x) for x in mylist]
    return list(map(int,mylist))

mylist : List[str] = ['1', '100', '33']
print(solution(mylist=mylist))