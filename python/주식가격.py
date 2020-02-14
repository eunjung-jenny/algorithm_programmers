# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             cnt += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(cnt)
#     return answer  


def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer


# 스택 활용 (by. 김태우)
# def solution(prices):
#     stack = []
#     result = [0 for _ in range(len(prices))]
#     for i in range(len(prices)):
#         while stack and prices[stack[-1]] > prices[i]:
#             x = stack.pop()
#             result[x] = i - x
#         stack.append(i)
#     while stack:
#         x = stack.pop()
#         result[x] = i - x
#     return result