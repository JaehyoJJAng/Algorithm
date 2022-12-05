import sys
# 양꼬치

def validation_check(n,k,type)-> any:
    if isinstance(n,type) and isinstance(k,type): 
        if 0 < n < 1000:
            pass
        else:
            print(f'{n} invalid')
            sys.exit()

        if int((n / 10)) <= k < 1000 :
            pass
        else:
            print(f'k:{k} invalid')
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(n:int,k:int):
    # Valication Check
    validation_check(n=n,k=k,type=int)
    
    if n >= 10:
        service= int(n // 10)
        return int((n * 12000) + (k * 2000 - (service * 2000)))
    else:
        return int((n * 12000) + (k * 2000))

print(solution(n=10,k=3))
