from typing import List
def solution(my_string: str) -> List[str]:
    answer : List[str] = sorted([my_string[i:] for i in range(len(my_string))])
    return answer

my_string : str = 'banana'
solution(my_string=my_string)