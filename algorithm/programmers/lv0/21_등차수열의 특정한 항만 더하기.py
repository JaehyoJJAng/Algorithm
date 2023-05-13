from typing import List
def solution(a: int,d: int,included: List[bool]) -> int:
    # answer = a
    # g = []
    # for i in range(len(included)):                
    #     if included[i]:
    #         g.append(answer)
    #     answer += d
    # return sum(g)\    
    return sum(a + i * d for i,f in enumerate(included) if f)

a : int = 3
d : int = 4
included : List[bool] = [True, False, False, True, True]
solution(a=a,d=d,included=included)