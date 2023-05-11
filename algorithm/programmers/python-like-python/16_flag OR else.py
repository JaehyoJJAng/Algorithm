import math 

mul = 1
for _ in range(5):
    mul *= int(input())
    if math.sqrt(mul) == int(math.sqrt(mul)):
        print("found")
        break 
else:
    print("not found")