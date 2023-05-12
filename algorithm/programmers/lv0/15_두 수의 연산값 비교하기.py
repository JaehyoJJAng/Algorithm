def solution(a: int,b: int) -> int:
    # return int(str(a) + str(b)) if int(str(a) + str(b)) >= 2 * a * b else 2 * a * b
    return max(int(str(a) + str(b) , 2 * a * b ))

a : int = 9
b : int = 91
print(solution(a=a,b=b))