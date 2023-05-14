from typing import Dict
def solution(n: int,control: str) -> int:
    # === 내 풀이 ===
    # answer : int = n    
    # for x in control:
    #     if "w" == x:
    #         answer += 1
    #     elif "s" == x:
    #         answer -= 1
    #     elif "d" == x:
    #         answer += 10
    #     else:
    #         answer -= 10        
    # return answer
    
    # === 다른 사람 풀이 ===
    answer : int = n
    c : Dict[str,int] = {'w':1, 's': -1, 'd': 10, 'a': -10}
    for i in control:
        answer += c[i]
    return answer

n : int = 0
control : str = "wsdawsdassw"
print(solution(n=n,control=control))