from typing import List

def solution(str_list: List[str]) -> List[str]:    
    l_index : int = str_list.index('l') if 'l' in str_list else float('inf')
    r_index : int = str_list.index('r') if 'r' in str_list else float('inf')
    
    if l_index < r_index: 
        return str_list[:l_index]
    elif r_index < l_index:
        return str_list[r_index + 1:]
    else :
        return []

str_list : List[str] = ['u','u','l','r']
solution(str_list=str_list)