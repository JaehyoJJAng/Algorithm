def solution(str1: str,str2: str) -> str:
    answer = ''    
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

str1 : str = 'aaaaa'
str2 : str = 'bbbbb'
solution(str1=str1,str2=str2)