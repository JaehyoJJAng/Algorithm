def solution(value: int,unit: str) -> int:
    converted : int = 0
    if unit == "C":
        value = int( (value * 1.8) + 32 )
    elif unit == "F":
        value = int( (value - 32) / 1.8 )    
    return value

value : int = 527
unit  : str = "C"
solution(value=value,unit=unit)