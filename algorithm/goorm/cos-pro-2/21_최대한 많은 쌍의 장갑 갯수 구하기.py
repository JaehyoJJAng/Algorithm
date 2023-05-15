from typing import List

max_product_number : int = 10

def func_a(gloves: List[int]):
    counter : List[int] = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        counter[x] += 1
    return counter

def solution(left_gloves: List[int], right_gloves: List[int]):
    left_counter  : List[int] = func_a(left_gloves) 
    right_counter : List[int] = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total

left_gloves  : List[int] = [2, 1, 2, 2, 4]
right_gloves : List[int] = [1, 2, 2, 4, 4, 7]
ret : int = solution(left_gloves, right_gloves)
print('solution 함수의 반환 값은', ret, '입니다.')