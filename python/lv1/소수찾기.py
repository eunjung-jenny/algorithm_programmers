N = 1000000
prime_nums = [1] * (N+2)
prime_nums[0] = 0
prime_nums[1] = 0

for i in range(2, (N+1)//2):
    for j in range(2*i, N+1, i):
        if prime_nums[j]:
            prime_nums[j] = 0

def solution(n):
    return sum(prime_nums[:n+1])
    
    

n = [10, 5]
result = [4, 3]

for i in range(len(n)):
    if solution(n[i]) == result[i]:
        print(f'{i}: pass')
    else:
        print(f'{i}: fail')