def solution(code: str) -> str:
    ret  : str = ''
    mode : int = 0
    for idx in range(len(code)):
        if mode:
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 1
        
        else:
            if code[idx] != "1" and idx % 2 == 1:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 0
    
    return ret if ret else "EMPTY"

code : str = "abc1abc1abc"
solution(code=code)