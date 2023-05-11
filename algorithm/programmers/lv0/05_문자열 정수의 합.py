def solution(num_str: str) -> int:
    return sum([int(num) for num in num_str])

num_str : str = "123456789"
print(solution(num_str=num_str))