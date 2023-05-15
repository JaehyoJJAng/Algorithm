def solution(number: int) -> int:
    # 내 풀이
    # d : int = len([x for x in str(number) if x in "2357"])
    # return d

    # 시험 풀이
    count : int = 0
    
    while number > 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10        
    print(count)        

number : int = 29022531
solution(number=number)