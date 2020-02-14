# by 김태우 똑똑하심
def solution(arrangement):
    answer = 0
    stack = 0
    for index, i in enumerate(arrangement):
        if i == ')' :
            stack -= 1
            if arrangement[index-1] == ')':
                answer += 1
            else:
                answer += stack
        else:
            stack += 1
    return answer