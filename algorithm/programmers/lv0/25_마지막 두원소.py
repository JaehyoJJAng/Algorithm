from typing import List

def solution(num_list: List[int]) -> List[int]:
    # length = len(num_list)
    # answer : List[int] = [0 for _ in range(2)]
    
    # for i in range(length):
    #     if i == length - 1:
    #         answer[-1] = num_list[i]
    #     elif i == length - 2:
    #         answer[0] = num_list[i]
    
    # if answer[-1] > answer[0]:
    #     num = answer[-1] - answer[0]
    #     num_list.append(num)
    # else:
    #     num = answer[-1] * 2
    #     num_list.append(num)
    
    # return num_list
    
    return num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] * 2)
    
num_list : List[int] = [5,2,1,7,5]
solution(num_list=num_list)