def func_a(number1: int,number2: int) -> int:
    ret = 0
    if number1 > number2:
        ret = number1 - number2
    else:
        ret = number2 - number1
    return ret

def func_b(number: int) -> int:
    ret = 0
    while number != 0:
        number = number // 10
        ret += 1
    return ret

def func_c(number: int,digit: int) -> int:
    ret = 0
    for i in range(digit):
        temp = number % 10
        number = number // 10
        ret = ret * 10 + temp
    return ret

def solution(number: int) -> None:
    answer = 0
    
    digit : int = func_b(number)
    convert_number : int = func_c(number=number,digit=digit)
    answer = func_a(number1=number,number2=convert_number)

number1 = 120
ret1 = solution(number1)