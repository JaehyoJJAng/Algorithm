from typing import List 

def solution(words: List[str]) -> str:
    answer : str = "".join([word for word in words if len(word) >= 5])
    return answer if answer else "empty"

words: List[str] = ["my", "favorite", "color", "is", "violet"]
solution(words=words)