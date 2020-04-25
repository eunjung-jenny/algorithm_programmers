from math import sqrt

def solution(n):
    if sqrt(n) == int(sqrt(n)):
        return (sqrt(n) + 1) ** 2
    else:
        return -1

N = [121, 3]
answer = [144, -1]

for i in range(len(N)):
    if solution(N[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')

# def nextSqure(n):
#     sqrt = n ** (1/2)

#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return 'no'

# def nextSqure(n):
#     return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'