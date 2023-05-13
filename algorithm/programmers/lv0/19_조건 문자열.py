def solution(ineq: str,eq: str,n: int,m: int) -> int:
    answer = 0
    if ineq == ">" and eq == "=":
        answer = 1 if n >= m else 0
    elif ineq == "<" and eq == "=":
        answer = 1 if n <= m else 0
    elif ineq == ">" and eq == "!":
        answer = 1 if n > m else 0
    else :
        answer = 1 if n < m else 0
    return answer

ineq : str = '<'
eq   : str = '='
n : int = 20
m : int = 50
solution(ineq=ineq,eq=eq,n=n,m=m)