def func_a(s) -> int:
    # 최고 점수 찾는 함수
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s) -> int:
    # 모든 과목 점수의 합 구하는 함수
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s) -> int:
    # 최저 점수 찾는 함수
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret

s = [100,25,30,65,85]

print(func_a(s=s)) # 100
print(func_b(s=s)) # 305
print(func_c(s=s)) # 25