def solution(my_string: str, overwrite_string: str, s: int) -> str:
    # my_string = list(my_string)
    # for idx in range(len(overwrite_string)):
    #     my_string[s + idx] = overwrite_string[idx]
    # return ''.join(my_string)
    
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string)]

my_string : str = 'He11oWor1d'
overwrite_string : str = 'lloWorl'
s : int = 2
solution(my_string=my_string,overwrite_string=overwrite_string,s=s)