# 편지


def validation_check(obj,type):
    if instance(obj,type):
        if 1 <= len(obj) <= 50 and re.match('[A-Za-z!~ ]',obj):
            pass
        else:
            print("String Error")
            sys.exit()
    else:
        print("Invalid Validation")
        sys.exit()

def solution(message:str):
    answer = 0
    
    message_length = len(message)
    return message_length * 2
