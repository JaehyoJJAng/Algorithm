from typing import List 

def func_a(scores: List[int],score: int) -> int: 
    """ 점수 찾기 """
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def func_b(arr: List[int]) -> None:
    """ 내림차순 정렬 """
    arr.sort(reverse=True)

def func_c(arr: List[int],n: int) -> int:
    """ n번 학생의 점수 리턴 """
    return arr[n]    
    
def solution(scores: List[int],n: int) -> int:
    score : int = func_c(arr=scores,n=n)
    func_b(arr=scores)
    answer = func_a(scores=scores,score=score)
    return answer

scores : List[int] = [20,60,98,59]
n : int = 3
print(solution(scores=scores,n=n))