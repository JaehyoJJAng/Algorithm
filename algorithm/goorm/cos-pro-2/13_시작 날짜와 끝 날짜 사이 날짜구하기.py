from typing import List

def solution(start_month: int, start_day: int, end_month: int, end_day: int) -> int:
	start_total : int = func_a(start_month, start_day)
	end_total   : int = func_a(end_month, end_day)
	return end_total - start_total


def func_a(month: int,day: int) -> int:
    month_list : List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total : int = 0
    
    for i in range(month - 1):
        total += month_list[i]
    
    total += day

    return total - 1        

start_month : int = 1
start_day : int = 2
end_month : int = 2
end_day : int = 2
ret = solution(start_month, start_day, end_month, end_day)
print(ret)