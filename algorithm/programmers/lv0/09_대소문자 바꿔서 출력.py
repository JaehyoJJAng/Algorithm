def solution(my_string):
    str = 'aBcDeFg'
    answer = ''
    for i in str:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()

def solution2(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])

my_string = 'aBcDeFg'
print(solution2(my_string=my_string))