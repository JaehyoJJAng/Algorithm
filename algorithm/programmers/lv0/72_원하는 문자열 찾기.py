def solution(myString: str, pat: str):
    myString = myString.upper()  # 대문자로 변환
    pat = pat.upper()  # 대문자로 변환

    for i in range(len(myString) - len(pat) + 1):
        substring = myString[i:i+len(pat)]
        if substring == pat:
            return 1
    
    return 0


myString : str = 'AbCdEfG'
pat: str = 'aBc'
solution(myString=myString,pat=pat)