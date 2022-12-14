from collections import deque
# 배열 회전 시키기

def solution(numbers,direction):
    numbers_deque = deque(numbers)
    
    # 풀이 (1)
#    if direction == 'right':
#        numbers_deque.rotate(1)
#    elif direction == 'left':
#        numbers_deque.rotate(-1)
#    return list(numbers_deque)

    # 풀이 (2)
    answer = [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
