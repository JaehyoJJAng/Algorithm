from typing import List

def solution(todo_list: List[str] , finished: List[bool]) -> List[str]:
    answer : List[str] = [todo_list[idx] for idx in range(len(todo_list)) if finished[idx] == False]
    return answer

todo_list : List[str] = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished : List[bool] = [True,False,True,False]
solution(todo_list=todo_list,finished=finished)