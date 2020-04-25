def solution(n):
    if n < 10:
        return n
    return n % 10 + solution(n//10)

N = [123, 987]
answer = [6, 24]

for i in range(len(N)):
    if solution(N[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')