def solution(a: int,b: int) -> int:
    return int(max(f"{a}{b}",f"{b}{a}"))
    
a : int = 89
b : int = 8
solution(a=a,b=b)