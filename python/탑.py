def solution(heights):
    answer = []
    for i in range(len(heights)):
        if i == 0:
            answer.append(0)
        else:
            stack = heights[:i]
            while stack:
                if stack.pop() > heights[i]:
                    answer.append(len(stack)+1)
                    break
            else:
                answer.append(0)
                
    return answer