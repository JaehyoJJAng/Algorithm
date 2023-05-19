def solution(my_string: str,n: int) -> None:
    answer = ''.join([my_string[i] for i in range(n)])    
    return answer
    # return my_string[:n]
    
my_string : str = "ProgrammerS123"
n : int = 11
solution(my_string=my_string,n=n)