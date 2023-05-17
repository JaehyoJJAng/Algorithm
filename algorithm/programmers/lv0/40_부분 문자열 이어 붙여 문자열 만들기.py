from typing import List

def solution(my_strings: List[str], parts: List[List[int]]) -> str:
    d : str = ''
    for i,(s,e) in enumerate(parts):
        d += my_strings[i][s:e+1]       
    return d

my_strings: List[str] = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts: List[List[int]] = [[0, 4], [1, 2], [3, 5], [7, 7]]
solution(my_strings=my_strings,parts=parts)