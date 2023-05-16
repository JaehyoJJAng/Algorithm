def solution(num_apple: int,num_carrot: int,k: int):
    answer : int = 0
    if num_apple < (3 * num_carrot):
        answer = num_apple // 3
    else:
        answer = num_carrot
    
    num_apple -= answer * 3
    num_carrot -= answer
    
    i = 0
    k = k - (num_apple + num_carrot)
    
    while k > 0:
        if i % 4 == 0:
            answer = answer - 1
        i = i + 1
        k = k - 1
    return answer

num_apple1  : int = 5
num_carrot1 : int = 1
k1 : int = 2
solution(num_apple1, num_carrot1, k1)