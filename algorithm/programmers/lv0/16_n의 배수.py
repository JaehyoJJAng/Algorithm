def solution(num: int,n: int) -> int:
    # return 1 if num % n == 0 else 0
    return int(not(num % n))

num : int = 34
n   : int = 3
print(solution(num=num,n=n))