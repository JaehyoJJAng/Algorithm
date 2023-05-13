def solution(a: int,b: int,c: int) -> int:
    answer = set([a,b,c])    
    if len(answer) == 3:
        return a + b + c
    
    elif len(answer) == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    
    else:
        return (a + b  + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    
a : int = 4
b : int = 4
c : int = 4
print(solution(a=a,b=b,c=c))