# 완전 탐색
# def solution(heights):
#     answer = []
#     for i in range(len(heights)):
#         if i == 0:
#             answer.append(0)
#         else:
#             stack = heights[:i]
#             while stack:
#                 if stack.pop() > heights[i]:
#                     answer.append(len(stack)+1)
#                     break
#             else:
#                 answer.append(0)
                
#     return answer

# 스택
def solution(heights):
    answer = []
    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[j] > heights[i]:
                stack.append(j+1)
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(0)
    return answer