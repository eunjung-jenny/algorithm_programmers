def solution(n, lost, reserve):
    clothes = [1]*n
    for id in lost:
        clothes[id-1] -= 1
    for id in reserve:
        clothes[id-1] += 1
    
    answer = 0
    for id in range(n):
        if clothes[id]:
            answer += 1
        else:
            if id-1 > 0 and clothes[id-1] > 1:
                clothes[id-1] -= 1
                clothes[id] += 1
                answer += 1
            elif id+1 < n and clothes[id+1] > 1:
                clothes[id+1] -= 1
                clothes[id] += 1
                answer += 1
            
    
    return answer

N = [5, 5, 3]
lost = [[2,4], [2,4], [3]]
reserve = [[1,3,5], [3], [1]]
answer = [5, 4, 2]

for i in range(len(N)):
    if solution(N[i], lost[i], reserve[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')