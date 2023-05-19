def solution(my_string: str,m: int,c: int) -> str:
    divided = [my_string[i:i + m] for i in range(0,len(my_string), m)]    
    column  = [divided[i][c - 1] for i in range(len(divided))]
    return ''.join(column)
my_string : str = "ihrhbakrfpndopljhygc"
m : int = 4
c : int = 2
solution(my_string=my_string,m=m,c=c)
