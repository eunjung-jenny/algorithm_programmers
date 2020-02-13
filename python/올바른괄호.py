def solution(s):
    answer = True
    stack = []
    
    for ss in s:
        if ss == '(':
            stack.append(ss)
        else:
            if not stack:
                answer = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                answer = False
                break
    else:
        if stack:
            answer = False    

    return answer

s = ')()('
print(solution(s))