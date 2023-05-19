from typing import List

def solution(my_string: str,s: int,e: int) -> str:
    string_list : List[str] = list(my_string)    
    substring   : List[str] = string_list[s:e + 1]
    
    # 부분 문자열 뒤집기
    substring.reverse()
    print(substring)
    
    # 원본 문자열에서 부분 문자열 대체    
    string_list[s: e + 1] = substring

    return "".join(string_list)    

my_string : str = "Progra21Sremm3"
s : int = 6
e : int = 12
solution(my_string=my_string,s=s,e=e)