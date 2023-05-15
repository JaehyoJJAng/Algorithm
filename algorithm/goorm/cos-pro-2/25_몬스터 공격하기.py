def solution(attack, recovery, hp):
    count = 0
    while(True):
        # 떄린 횟수 카운트
        count += 1
        
        # 몬스터 공격
        hp -= attack
        if hp <= 0:
            print("몬스터가 죽었습니다")
            break
        
        # 몬스터의 힐 마법 사용
        hp += recovery
    return count

attack : int = 30
recovery : int = 10
hp : int = 60
solution(attack=attack,recovery=recovery,hp=hp)