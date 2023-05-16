from typing import List

def solution(words: List[str],word: str) -> str:
    count : int = 0    
    for o,i in enumerate(words):
        for idx,j in enumerate(i):
            if word[idx] != j:
                count += 1
    return count

	# count = 0
	# for x in words:
	# 	for y in range(len(word)):
	# 		if x[y] != word[y]: 
	# 			count += 1
	# return count

    
words : List[str] = ["CODE", "COED", "CDEO"]
word : str = "CODE"
solution(words=words,word=word)