def solution(my_string: str, is_suffix: str) -> int:
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            answer = 1
            break
    
    return answer
    
my_string : str = "banana"
is_suffix : str = "ana"
print(solution(my_string=my_string,is_suffix=is_suffix))