def solution(a: int,b: int,flag: bool) -> int:
    return a + b if flag else a - b
    
a : int = -4
b : int = 7
flag : bool = False
print(solution(a=a,b=b,flag=flag))