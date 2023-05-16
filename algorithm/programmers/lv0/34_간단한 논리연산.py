def solution(x1: bool,x2: bool,x3: bool,x4: bool) -> bool:
    return (x1 | x2) & (x3 | x4)
    # return (x1 or x2) and (x3 or x4)