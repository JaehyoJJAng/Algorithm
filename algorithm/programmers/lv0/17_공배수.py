def solution(number: int,n: int,m: int) -> int:
    return int(True) if number % n == 0 and number % m == 0 else int(False)

number : int = 55
n : int = 10
m : int = 5
print(solution(number=number,n=n,m=m))