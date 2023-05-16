def solution(number: str) -> int:
    # return  sum(list(map(int,list(number))))
    return sum([int(num) for num in number]) % 9

number : str = "78720646226947352489"
solution(number=number)