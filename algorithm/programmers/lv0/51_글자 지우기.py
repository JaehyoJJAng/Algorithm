from typing import List

def solution(my_string: str,indices: List[int]) -> str:
    my_string = list(my_string)
    answer = ''
    
    for i in range(len(my_string)):
        if i not in indices: 
            answer += my_string[i]
    return answer        

my_string : str = "apporoograpemmemprs"
indices : List[int] = [1, 16, 6, 15, 0, 10, 11, 3]
solution(my_string=my_string,indices=indices)