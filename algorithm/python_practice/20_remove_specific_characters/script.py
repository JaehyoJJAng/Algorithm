import re
# 특정 문자 제거하기


def validation_check(string,letter,type):
    if isinstance(string,type) and isinstance(letter,type):
        if 1 <= len(string) <= 100 and len(letter) == 1:
            pass
        else:
            print("Num Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(my_string:str,letter:str):
    # Validation Check
    validation_check(string=my_string,letter=letter,type=str)
    return re.sub(f'{letter}','',my_string)

    #new_string = my_string.replace(letter,'')
    #print(new_string)
