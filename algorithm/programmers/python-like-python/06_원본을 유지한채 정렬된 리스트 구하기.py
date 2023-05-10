from typing import List

# list1 : List[int] = [3,2,5,1]
# list2 : List[int] = [i for i in list1]
# list2.sort()

# ====

list1 : List[int] = [3,2,5,1]
list2 : List[int] = sorted(list1)
print(list2)