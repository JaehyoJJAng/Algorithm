import re
# 문자열 정렬하기 (1)


def solution(my_string):
    return sorted([int(n) for n in list(re.sub('[^0-9]','',my_string))])

solution(my_string='hi12392')
solution(my_string='p2o4i8gj2')
solution(my_string='abcde0')

