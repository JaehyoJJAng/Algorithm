def solution(my_string: str,n: int) -> str:
    answer : str = my_string.replace(my_string[:-n],'')
    # answer : str =  my_string[-n:]
    return answer

my_string : str = "He110W0r1d"
n : int = 5
solution(my_string=my_string,n=n)