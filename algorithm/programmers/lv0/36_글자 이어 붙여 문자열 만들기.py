from typing import List

def solution(my_string: str,index_list: List[int]) -> str:
    answer : str = "".join([my_string[i] for i in index_list])
    return answer

my_string : str = "cvsgiorszzzmrpaqpe"
index_list : List[int] = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
solution(my_string=my_string,index_list=index_list)