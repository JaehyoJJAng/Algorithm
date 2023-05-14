from typing import List,Dict

def solution(numLog: List[int]) -> str:
    answer : str = ""
    c : Dict[int,str] = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    for i in range(1,len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        answer += c[diff]
    return answer

numLog : List[int] = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
solution(numLog=numLog)