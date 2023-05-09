from typing import List

def solution(s: str) -> str:
    s_lst : List[str] = list(s) # ['a','b','z']
    n = len(s) # 3
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] =  'a'
    
    return "".join(s_lst)

s : str = "abz"
solution(s=s)