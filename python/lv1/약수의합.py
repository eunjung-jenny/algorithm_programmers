def solution(n):
    answer = 0
    for num in range(1, n+1):
        if not(n % num):
            answer += num
    return answer