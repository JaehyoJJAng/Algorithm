from typing import List
def solution(q: int,r: int,code: str) -> str:
    answer : List[str] = [code[i] for i in range(len(code)) if i % q == r]
    return ''.join(answer)
    
q : int = 3
r : int = 1
code : str = 'qjnwezgrpirldywt'
solution(q=q,r=r,code=code)