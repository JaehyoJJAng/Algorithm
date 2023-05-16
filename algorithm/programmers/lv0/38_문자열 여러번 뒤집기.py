from typing import List

def solution(my_string: str,queries: List[List[int]]) -> str:
    strings : List[str] = list(my_string)
    for s,e in queries:
        strings[s:e+1] = strings[s:e+1][::-1]
    return ''.join(strings)

my_string : str = "rermgorpsam"
queries   : List[List[int]] = [[2, 3], [0, 7], [5, 9], [6, 10]]
solution(my_string=my_string,queries=queries)