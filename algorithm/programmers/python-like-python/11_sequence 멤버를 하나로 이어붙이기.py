from typing import List

def solutuon(mylist: List[str]) -> str:
    return "".join([d for d in mylist])

mylist : List[str] = ['1','100','33']
print(solutuon(mylist=mylist))