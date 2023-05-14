def solution(number: int) -> int:
    count : int = 0
    for i in range(1, number + 1):
        # 현재 숫자 위치 
        current : int = i

        while current != 0:
            # 3의 배수인 경우
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                # 카운트 (박수) 증감
                count += 1
            current = current // 10
    return count