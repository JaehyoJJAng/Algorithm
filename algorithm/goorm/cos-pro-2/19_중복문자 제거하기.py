def solution(characters: str) -> str:
    result : str = ""
    for i in range(len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

characters : str = "senteeeencccccceeee"
ret : str = solution(characters)
print("solution 함수의 반환 값은", ret, "입니다.")