def solution(n: int) -> int:
    answer : int = 0    
    return sum([i ** 2 for i in range(1 , n + 1) if i % 2 == 0]) if n % 2 == 0 else sum(i for i in range(1, n + 1) if i % 2 == 1)

n : int = 10
print(solution(n=n))