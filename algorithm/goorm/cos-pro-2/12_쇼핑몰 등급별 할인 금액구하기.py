def solution(price: int,grade: str) -> int:
    answer : int = 0 
    
    if "S" == grade  : answer = price - int(abs(price * 0.05))
    elif "G" == grade: answer = price - int(abs(price * 0.1))
    elif "V" == grade: answer = price - int(abs(price * 0.15))
    return answer

price : int = 2500
grade : str = "V"
print(solution(price=price,grade=grade))