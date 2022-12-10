import sys
# 배열의 유사도


def validation_check(s1,s2,type):
    if isinstance(s1,type) and isinstance(s2,type):
        s1_ch = [_.lower() for _ in s1 if 1 <= len(_) <= 10]
        s2_ch = [_.lower() for _ in s1 if 1 <= len(_) <= 10]

def solution(s1:list,s2:list):
    # Validation Check
    validation_check(s1=s1,s2=s2,type=list)
    
    s1.extend(s2)
    return len(s1) - len(list(set(s1)))
