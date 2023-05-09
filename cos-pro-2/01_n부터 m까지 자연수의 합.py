def func_a(k) -> None:
    sum : int = 0
    for i in range(1,k + 1):
        sum += i 
    return sum

def solution(n,m)-> None:
    # 1부터 m까지의 합 구하기
    sum_to_m : int = func_a(k=m)
    
    # 1부터 n까지의 합 구하기
    sum_to_n : int = func_a(k=n-1)
    
    # m의 합 - n의 합
    result : int = sum_to_m - sum_to_n
    
    return result