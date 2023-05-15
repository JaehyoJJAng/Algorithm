def solution(N: int,M: int) -> int: 
    answer : int = sum([i ** 2 for i in range(N, M + 1) if i % 2 == 0])
    return answer

N : int = 4
M : int = 7
print(solution(N=N,M=M))