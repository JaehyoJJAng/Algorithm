def solution(password: str) -> bool:
    capital_count , small_count , digit_count = 0,0,0
    
    for p in password:
        if p >= 'A' and p <= 'Z':
            capital_count += 1
        elif p >= 'a' and p <= 'z':
            small_count += 1
        elif int(p) >= 0 and int(p) <= 9:
            digit_count += 1
    
    if capital_count and small_count and digit_count:
        answer = True
    else:
        answer = False    
    return True if answer else False

password : str = 'Hello123'
solution(password=password)