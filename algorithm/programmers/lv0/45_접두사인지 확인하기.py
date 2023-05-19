def solution(my_string: str,is_prefix: str) -> int:
    answer = [1 if my_string[:i] == is_prefix else 0 for i in range(len(my_string))]
    return 1 if 1 in answer else 0

my_string : str = "banana"
is_prefix : str = "ban"
solution(my_string=my_string,is_prefix=is_prefix)