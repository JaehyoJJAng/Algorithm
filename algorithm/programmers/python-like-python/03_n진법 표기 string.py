num, base = map(int, input().split())
answer = 0
num = str(num)
for idx, i in enumerate(num[::-1]):
    answer += int(i) * (base ** idx)
print(answer)