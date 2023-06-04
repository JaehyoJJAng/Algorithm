from typing import List

def solution(n: int,slicer: List[int],num_list: List[int]) -> List[int]:
    answer : List[int] = []
    a : int = slicer[0]
    b : int = slicer[1]
    c : int = slicer[-1]
    
    if n == 1:
        t : List[int] = num_list[:b + 1]
    elif n == 2:        
        t : List[int] = num_list[a:]
    elif n == 3:
        t : List[int] = num_list[a:b + 1]
    elif n == 4:
        # t : List[int] = [t for t in num_list[a:b + 1] if t % c == 0]
        t : List[int] = num_list[a:b + 1:c]
    return answer
    
n : int = 4
slicer : List[int] = [1,5,2]  # a , b, c
num_list : List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
solution(n=n,slicer=slicer,num_list=num_list)