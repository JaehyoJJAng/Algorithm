from typing import List

def solution(num_list: List[int]) -> List[int]:        
    # === 내 풀이 ===
    # if num_list[-1] > num_list[-2]:
    #     num_list.append(num_list[-1] - num_list[-2])
    # else:
    #     num_list.append(num_list[-1] * 2)
    # return num_list

    # === 다른 사람 풀이 ===\
    return num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] * 2)
    
num_list : List[int] = [5,2,1,7,5]
solution(num_list=num_list)